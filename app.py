from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

# Sample Bus Data (Fake GPS Data)
bus_data = {
    "101": {
        "route": "Chennai to Coimbatore",
        "scheduled_time": "15:00",
        "current_location": "Salem",
        "delay_minutes": 20
    },
    "102": {
        "route": "Madurai to Trichy",
        "scheduled_time": "14:30",
        "current_location": "Dindigul",
        "delay_minutes": 5
    }
}

@app.route("/", methods=["GET", "POST"])
def home():
    bus_info = None
    if request.method == "POST":
        bus_number = request.form["bus_number"]
        if bus_number in bus_data:
            bus_info = bus_data[bus_number]
            scheduled = datetime.strptime(bus_info["scheduled_time"], "%H:%M")
            new_time = scheduled + timedelta(minutes=bus_info["delay_minutes"])
            bus_info["expected_arrival"] = new_time.strftime("%H:%M")
    return render_template("index.html", bus_info=bus_info)

if __name__ == "__main__":
    app.run(debug=True)
