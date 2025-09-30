from flask import Flask, render_template, request, jsonify
import networkx as nx
import heapq

app = Flask(__name__)

# -------------------------
# Graph of Hyderabad areas
# -------------------------
G = nx.Graph()
cities = [
    "Hyderabad", "Secunderabad", "LB Nagar", "Banjara Hills", 
    "Gachibowli", "Hitech City", "Medchal", "Miyapur"
]

# Edges with approximate distances (in km)
edges = [
    ("Hyderabad", "Secunderabad", 8),
    ("Hyderabad", "Banjara Hills", 5),
    ("Hyderabad", "LB Nagar", 12),
    ("Banjara Hills", "Gachibowli", 10),
    ("Gachibowli", "Hitech City", 5),
    ("Hitech City", "Miyapur", 8),
    ("Secunderabad", "Medchal", 20),
    ("LB Nagar", "Gachibowli", 15),
    ("Medchal", "Miyapur", 22),
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# -------------------------
# Heuristic for A* (straight-line approx to Hitech City)
# -------------------------
heuristic = {
    "Hyderabad": 10,
    "Secunderabad": 12,
    "LB Nagar": 15,
    "Banjara Hills": 8,
    "Gachibowli": 5,
    "Hitech City": 0,
    "Medchal": 18,
    "Miyapur": 7
}

# -------------------------
# A* Algorithm
# -------------------------
def astar_graph(G, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor in G.neighbors(current):
            cost = G[current][neighbor]['weight']
            if neighbor not in visited:
                heapq.heappush(open_set, (g + cost + heuristic[neighbor], g + cost, neighbor, path + [neighbor]))
    return None

# -------------------------
# Flask Routes
# -------------------------
@app.route("/")
def index():
    return render_template("index.html", cities=cities)

@app.route("/get_route", methods=["POST"])
def get_route():
    start = request.form.get("start")
    end = request.form.get("end")
    if start not in G.nodes or end not in G.nodes:
        return jsonify({"route": None, "error": "Invalid city names!"})
    path = astar_graph(G, start, end, heuristic)
    return jsonify({"route": path})

if __name__ == "__main__":
    app.run(debug=True)
