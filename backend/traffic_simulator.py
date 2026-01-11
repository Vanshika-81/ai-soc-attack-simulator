# =========================================================
# Traffic simulation logic
# =========================================================
import random
import time
from datetime import datetime

# =========================================================
# Traffic Event Definition (SOC-observable event)
# =========================================================
class TrafficEvent:
    def __init__(self, src_ip, dst_ip, dst_port, packet_rate, traffic_type):
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.packet_rate = packet_rate
        self.traffic_type = traffic_type

    def to_dict(self):
        return {
            "time": self.timestamp,
            "src_ip": self.src_ip,
            "dst_ip": self.dst_ip,
            "dst_port": self.dst_port,
            "packet_rate": self.packet_rate,
            "type": self.traffic_type
        }

# =========================================================
# Utility Functions
# =========================================================
def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

TARGET_IP = "192.168.1.10"

# =========================================================
# Traffic Generators
# =========================================================
def generate_normal_traffic():
    return TrafficEvent(
        src_ip=random_ip(),
        dst_ip=TARGET_IP,
        dst_port=80,
        packet_rate=random.randint(10, 40),
        traffic_type="normal"
    )

def generate_ddos_traffic(intensity):
    return TrafficEvent(
        src_ip=random_ip(),
        dst_ip=TARGET_IP,
        dst_port=80,
        packet_rate=int(random.randint(300, 600) * intensity),
        traffic_type="ddos"
    )

def generate_bruteforce_traffic(intensity):
    return TrafficEvent(
        src_ip="10.0.0.5",
        dst_ip=TARGET_IP,
        dst_port=22,
        packet_rate=int(random.randint(40, 80) * intensity),
        traffic_type="bruteforce"
    )

def generate_portscan_traffic():
    return TrafficEvent(
        src_ip="10.0.0.9",
        dst_ip=TARGET_IP,
        dst_port=random.randint(1, 1024),
        packet_rate=random.randint(5, 15),
        traffic_type="portscan"
    )

# =========================================================
# SOC State (threshold + metrics tracking)
# =========================================================
bruteforce_attempts = 0
scanned_ports = set()

# SOC metrics
total_events = 0
attack_events = 0
alerts_triggered = 0

# =========================================================
# AI-DRIVEN SIMULATOR LOOP
# =========================================================
if __name__ == "__main__":

    intensity = 1.0   # attacker aggressiveness (adaptive)

    for step in range(120):

        alert = False
        total_events += 1

        # -------------------------------
        # Traffic Timeline / Scenario
        # -------------------------------
        if step < 30:
            # Normal baseline traffic
            event = generate_normal_traffic()

        elif step < 60:
            # DDoS-like volumetric traffic
            event = generate_ddos_traffic(intensity)
            if event.packet_rate > 400:
                alert = True

        elif step < 90:
            # Brute-force traffic
            event = generate_bruteforce_traffic(intensity)
            bruteforce_attempts += 1
            if bruteforce_attempts > 10:
                alert = True

        else:
            # Port scanning traffic
            event = generate_portscan_traffic()
            scanned_ports.add(event.dst_port)
            if len(scanned_ports) > 20:
                alert = True

        # -------------------------------
        # SOC Metrics Update
        # -------------------------------
        if event.traffic_type != "normal":
            attack_events += 1

        if alert:
            alerts_triggered += 1

        # -------------------------------
        # AI Adaptation Logic
        # -------------------------------
        if alert:
            intensity *= 0.9    # SOC detected → attacker backs off
        else:
            intensity *= 1.1    # SOC missed → attacker escalates

        intensity = max(0.5, min(intensity, 2.0))

        print(event.to_dict())
        time.sleep(0.3)

    # =====================================================
    # SOC RESILIENCE SUMMARY
    # =====================================================
    print("\n--- SOC RESILIENCE SUMMARY ---")
    print(f"Total Events: {total_events}")
    print(f"Attack Events: {attack_events}")
    print(f"Alerts Triggered: {alerts_triggered}")

    if attack_events > 0:
        detection_rate = (alerts_triggered / attack_events) * 100
        print(f"Detection Rate: {detection_rate:.2f}%")
    else:
        print("Detection Rate: N/A")
