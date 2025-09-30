
## 3️⃣ `app.py`
from flask import Flask, render_template, request, jsonify
import networkx as nx
import heapq

app = Flask(__name__)

# ---------------- Graph of Hyderabad areas ----------------
G = nx.Graph()
cities = [
    "Hyderabad", "Secunderabad", "LB Nagar", "Banjara Hills",
    "Gachibowli", "Hitech City", "Medchal", "Miyapur",
    "Kukatpally", "Ameerpet", "Begumpet", "Tolichowki",
    "Nampally", "Madhapur", "Jubilee Hills", "Nacharam",
    "Malkajgiri", "Kompally", "Uppal", "Dilsukhnagar"
]

edges = [
    ("Hyderabad", "Secunderabad", 8),
    ("Hyderabad", "Banjara Hills", 5),
    ("Hyderabad", "LB Nagar", 12),
    ("Hyderabad", "Nampally", 6),
    ("Banjara Hills", "Gachibowli", 10),
    ("Banjara Hills", "Jubilee Hills", 4),
    ("Gachibowli", "Hitech City", 5),
    ("Hitech City", "Miyapur", 8),
    ("Hitech City", "Madhapur", 2),
    ("Secunderabad", "Medchal", 20),
    ("LB Nagar", "Gachibowli", 15),
    ("Miyapur", "Kukatpally", 7),
    ("Kukatpally", "Ameerpet", 6),
    ("Ameerpet", "Begumpet", 4),
    ("Begumpet", "Secunderabad", 3),
    ("Tolichowki", "Gachibowli", 7),
    ("Tolichowki", "LB Nagar", 11),
    ("Nacharam", "LB Nagar", 10),
    ("Nacharam", "Madhapur", 18),
    ("Malkajgiri", "Secunderabad", 6),
    ("Kompally", "Medchal", 7),
    ("Uppal", "LB Nagar", 5),
    ("Dilsukhnagar", "LB Nagar", 4),
    ("Uppal", "Dilsukhnagar", 3),
    ("Jubilee Hills", "Madhapur", 3)
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Approximate heuristic distances to Hitech City
heuristic = {
    "Hyderabad": 10, "Secunderabad": 12, "LB Nagar": 15, "Banjara Hills": 8,
    "Gachibowli": 5, "Hitech City": 0, "Medchal": 18, "Miyapur": 7,
    "Kukatpally": 6, "Ameerpet": 5, "Begumpet": 6, "Tolichowki": 9,
    "Nampally": 8, "Madhapur": 2, "Jubilee Hills": 3, "Nacharam": 12,
    "Malkajgiri": 13, "Kompally": 16, "Uppal": 14, "Dilsukhnagar": 15
}

# ---------------- A* Algorithm ----------------
def astar_graph(G, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (heuristic.get(start, 0), 0, start, [start]))
    g_score = {start: 0}

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        for neighbor in G.neighbors(current):
            cost = G[current][neighbor]['weight']
            new_g = g + cost
            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                f_score = new_g + heuristic.get(neighbor, 0)
                heapq.heappush(open_set, (f_score, new_g, neighbor, path + [neighbor]))
    return None

# ---------------- Flask Routes ----------------
@app.route("/")
def index():
    return render_template("index.html", cities=cities)

@app.route("/get_route", methods=["POST"])
def get_route():
    city_map = {c.lower(): c for c in cities}

    start_raw = request.form.get("start", "").strip().lower()
    end_raw = request.form.get("end", "").strip().lower()

    if start_raw not in city_map or end_raw not in city_map:
        return jsonify({
            "success": False,
            "error": f"Invalid city name(s). Choose from: {', '.join(cities)}"
        }), 400

    start = city_map[start_raw]
    end = city_map[end_raw]

    path = astar_graph(G, start, end, heuristic)

    if path:
        total_distance = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
        return jsonify({
            "success": True,
            "path": path,
            "total_distance": total_distance
        })
    else:
        return jsonify({"success": False, "error": "No route found!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
