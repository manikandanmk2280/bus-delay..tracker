from flask import Flask, render_template, request
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# -----------------------------
# Bus Routes
# -----------------------------
routes = [
    "Chennai to Coimbatore",
    "Madurai to Trichy",
    "Salem to Chennai",
    "Erode to Madurai",
    "Trichy to Coimbatore",
    "Chennai to Vellore",
    "Vellore to Salem",
    "Coimbatore to Madurai"
]

locations = [
    "Bus Stand",
    "Highway",
    "Near Toll Gate",
    "City Center",
    "Bridge",
    "Terminal"
]

# -----------------------------
# Create 40 Bus Dataset
# -----------------------------
bus_data = {}

for i in range(1, 41):
    bus_number = f"TN{1000 + i}"

    scheduled_time = datetime.now() + timedelta(minutes=random.randint(10, 120))

    bus_data[bus_number] = {
        "bus_number": bus_number,
        "route": random.choice(routes),
        "scheduled_time": scheduled_time.strftime("%H:%M"),
        "current_location": random.choice(locations),
        "delay_minutes": random.randint(0, 20),
        "capacity": random.randint(30, 50)
    }

# -----------------------------
# Home Page
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    bus_info = None

    if request.method == "POST":
        bus_number = request.form.get("bus_number")

        if bus_number in bus_data:
            bus_info = bus_data[bus_number]

    return render_template(
        "index.html",
        bus_data=bus_data,
        bus_info=bus_info
    )

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
