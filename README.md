# 🗺️ Hyderabad Route Finder

A modern **Flask + NetworkX web app** that finds the shortest route between cities and towns around Hyderabad using the **A* Search Algorithm**.  

Users can type in start and destination cities to get the optimal path along with the total distance.

---

## 🚀 Features

- Chatbot-style interface.
- Calculate shortest path between 20 major Hyderabad neighborhoods.
- Displays total distance in kilometers.
- Handles invalid city names gracefully.
- Dynamic scrollable chat interface using Bootstrap + jQuery.

---

## 🏙️ Available Cities / Towns

Hyderabad, Secunderabad, LB Nagar, Banjara Hills, Gachibowli, Hitech City, Medchal, Miyapur, Kukatpally, Ameerpet, Begumpet, Tolichowki, Nampally, Madhapur, Jubilee Hills, Nacharam, Malkajgiri, Kompally, Uppal, Dilsukhnagar

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/hyderabad-route-finder.git
cd hyderabad-route-finder
Install dependencies:

bash:
Copy code
pip install -r requirements.txt
Run the Flask server:

bash:
Copy code
python app.py
Open the app in your browser:

cpp
Copy code
http://127.0.0.1:5000
💬 Usage:
Type a query in the format:

css:
Copy code
StartCity to EndCity
Example:

css:
Copy code
Hyderabad to Tolichowki
Uppal to Hitech City
The app will return:

✅ The optimal route.

📏 Total distance in km.

