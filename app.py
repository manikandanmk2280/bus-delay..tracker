from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import random

app = Flask(__name__)

bus_data = {}

routes = [
    "Chennai to Coimbatore",
    "Madurai to Trichy",
    "Salem to Erode",
    "Chennai to Madurai",
    "Trichy to Coimbatore"
]

locations = [
    "Vellore", "Salem", "Dindigul",
    "Namakkal", "Karur", "Tiruppur"
]

# Generate buses
for i in range(20):
    plate = f"TN{random.randint(1, 99):02d}AB{random.randint(1000,9999)}"
    bus_data[plate] = {
        "route": random.choice(routes),
        "scheduled_time": f"{random.randint(6,22):02d}:{random.randint(0,59):02d}",
        "current_location": random.choice(locations),
        "delay_minutes": random.randint(0,30),
        "capacity": random.randint(30,60)
    }

@app.route("/", methods=["GET", "POST"])
def home():
    bus_info = None

    if request.method == "POST":
        plate = request.form["bus_number"]

        if plate in bus_data:
            bus_info = bus_data[plate]
            scheduled = datetime.strptime(bus_info["scheduled_time"], "%H:%M")
            new_time = scheduled + timedelta(minutes=bus_info["delay_minutes"])

            bus_info["expected_arrival"] = new_time.strftime("%H:%M")
            bus_info["status"] = "Delayed" if bus_info["delay_minutes"] > 0 else "On Time"

    return render_template("index.html", bus_info=bus_info, buses=bus_data)

@app.route("/add", methods=["POST"])
def add_bus():
    plate = request.form["plate"]

    bus_data[plate] = {
        "route": request.form["route"],
        "scheduled_time": request.form["scheduled_time"],
        "current_location": request.form["location"],
        "delay_minutes": int(request.form["delay"]),
        "capacity": int(request.form["capacity"])
    }

    return redirect(url_for("home"))

@app.route("/delete/<plate>")
def delete_bus(plate):
    if plate in bus_data:
        del bus_data[plate]

    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

