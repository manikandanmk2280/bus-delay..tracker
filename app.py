from flask import Flask, render_template, request
import random
from datetime import datetime, timedelta
import os

app = Flask(__name__)

routes = [
    "Chennai to Coimbatore",
    "Madurai to Trichy",
    "Salem to Chennai",
    "Erode to Madurai",
    "Trichy to Coimbatore",
    "Chennai to Vellore",
    "Vellore to Salem",
    "Madurai to Chennai"
]

locations = [
    "Chennai", "Madurai", "Trichy", "Salem",
    "Erode", "Coimbatore", "Vellore"
]

bus_data = {}

for i in range(1, 41):
    bus_number = f"BUS{i:03}"

    scheduled_time = datetime.now() + timedelta(minutes=random.randint(5, 120))
    delay = random.randint(0, 30)

    bus_data[bus_number] = {
        "route": random.choice(routes),
        "scheduled_time": scheduled_time.strftime("%H:%M"),
        "current_location": random.choice(locations),
        "delay_minutes": delay,
        "capacity": random.randint(30, 50)
    }

@app.route("/", methods=["GET", "POST"])
def home():
    bus_info = None
    if request.method == "POST":
        bus_number = request.form["bus_number"]
        bus_info = bus_data.get(bus_number.upper())
    return render_template("index.html", bus_info=bus_info)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
