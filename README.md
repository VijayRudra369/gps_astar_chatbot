Smart GPS Chatbot

This project is a hybrid GPS chatbot that combines the A* algorithm for route finding with a Language Model (LLM) for natural language understanding. Users can enter start and destination areas, and the chatbot provides the shortest path if the cities exist in the graph. For any city outside the graph or general questions, the LLM gives intelligent, conversational replies.

Features:
- Modern web interface with chat bubbles.
- Shortest path calculation using A* algorithm for known cities.
- LLM integration for any city or general queries.
- Human-friendly explanations of routes.
- Easily extendable for more cities and smarter LLM responses.

Installation & Run:
1. Clone the repository:
   git clone https://github.com/VijayRudra369/gps_astar_chatbot.git

2. Navigate to the project folder:
   cd gps_astar_chatbot

3. Install dependencies:
   pip install -r requirements.txt

4. Run the chatbot:
   python app.py

5. Open your browser at http://127.0.0.1:5000/ to use the chatbot.

Future Improvements:
- Integrate a local LLM (LLAMA) for smarter conversational replies.
- Add more cities and real-world GPS data.
- Enhance frontend with timestamps, avatars, and responsive design.

Project Structure:
gps_astar_chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
