from flask import Flask, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

current_mode = "normal"
ALL_MODES = ["normal", "portscan", "bruteforce", "ddos"]

@app.route("/mode/<mode>", methods=["POST"])
def set_mode(mode):
    global current_mode
    if mode in ALL_MODES or mode == "mixed":
        current_mode = mode
    else:
        current_mode = "normal"

    return jsonify({"mode": current_mode})

@app.route("/event")
def generate_event():
    global current_mode

    # ⭐ TRUE MIXED (backend-controlled)
    mode = random.choice(ALL_MODES) if current_mode == "mixed" else current_mode

    timestamp = time.strftime("%H:%M:%S")
    src_ip = f"{random.randint(10,200)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

    if mode == "normal":
        packet_rate = random.randint(5, 20)
        dst_port = random.choice([80, 443])
        alert = False

    elif mode == "portscan":
        packet_rate = random.randint(30, 70)
        dst_port = random.randint(1, 1024)
        alert = True

    elif mode == "bruteforce":
        packet_rate = random.randint(40, 90)
        dst_port = 22
        alert = True

    elif mode == "ddos":
        packet_rate = random.randint(150, 400)
        dst_port = 80
        alert = True

    return jsonify({
        "time": timestamp,
        "src_ip": src_ip,
        "dst_port": dst_port,
        "packet_rate": packet_rate,
        "type": mode,
        "alert": alert
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
