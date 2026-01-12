from traffic_simulator import *
import random

current_mode = "normal"

stats = {
    "normal": 0,
    "attack": 0,
    "alerts": 0
}

def set_mode(mode):
    global current_mode
    current_mode = mode

def detect_attack(event):
    if event["type"] == "normal":
        return False
    if event["packet_rate"] > 200:
        return True
    if event["type"] in ["portscan", "bruteforce"]:
        return True
    return False

def get_next_event():
    if current_mode == "normal":
        event = generate_normal_traffic()
    elif current_mode == "portscan":
        event = generate_portscan_traffic()
    elif current_mode == "bruteforce":
        event = generate_bruteforce_traffic()
    elif current_mode == "ddos":
        event = generate_ddos_traffic()
    elif current_mode == "mixed":
        event = generate_mixed_traffic()
    else:
        event = generate_normal_traffic()

    is_attack = detect_attack(event)
    event["alert"] = is_attack

    if is_attack:
        stats["attack"] += 1
        stats["alerts"] += 1
    else:
        stats["normal"] += 1

    total = stats["normal"] + stats["attack"]
    resilience = max(0, int(100 - (stats["alerts"] / max(1, total)) * 100))

    event["stats"] = {
        "normal": stats["normal"],
        "attack": stats["attack"],
        "alerts": stats["alerts"],
        "resilience": resilience
    }

    return event
