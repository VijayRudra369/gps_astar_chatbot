from flask import Flask, render_template, request, jsonify
import networkx as nx
import heapq

# Optional: LLM integration (replace with LLAMA or GPT)
# Example: from llama_cpp import Llama
# llm = Llama(model_path="path_to_your_llama_model.bin")

app = Flask(__name__)

# ------------------------- Graph for Cities -------------------------
G = nx.Graph()
cities = ["Hyderabad", "Secunderabad", "LB Nagar", "Banjara Hills", 
          "Gachibowli", "Hitech City", "Medchal", "Miyapur"]

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

heuristic = {
    "Hyderabad": 10, "Secunderabad": 12, "LB Nagar": 15, "Banjara Hills": 8,
    "Gachibowli": 5, "Hitech City": 0, "Medchal": 18, "Miyapur": 7
}

# ------------------------- A* Algorithm -------------------------
def astar_graph(G, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (heuristic.get(start, 0), 0, start, [start]))
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
                heapq.heappush(open_set, (g + cost + heuristic.get(neighbor, 0), g + cost, neighbor, path + [neighbor]))
    return None

# ------------------------- LLM Placeholder Function -------------------------
def ask_llm(question):
    # Replace this with your local LLAMA/GPT API call
    return f"LLM says: {question} (smart response for any city or question)."

# ------------------------- Flask Routes -------------------------
@app.route("/")
def index():
    return render_template("index.html", cities=cities)

@app.route("/get_route", methods=["POST"])
def get_route():
    user_input = request.form.get("start").strip()
    destination = request.form.get("end").strip()

    # Check if both cities exist in the graph
    if user_input in G.nodes and destination in G.nodes:
        path = astar_graph(G, user_input, destination, heuristic)
        if path:
            # Format route in human-friendly text
            route_text = f"Start from {path[0]}, then go through " + ", ".join(path[1:-1]) + f", finally reach {path[-1]}."
            # Optional: LLM can improve this sentence
            # route_text = ask_llm(f"Explain the route: {' -> '.join(path)}")
            return jsonify({"route": route_text})
        else:
            return jsonify({"route": None, "error": "No route found!"})
    
    # If cities not in graph, fallback to LLM
    question = f"User asked about route from {user_input} to {destination}"
    llm_response = ask_llm(question)
    return jsonify({"route": None, "error": llm_response})

if __name__ == "__main__":
    app.run(debug=True)
