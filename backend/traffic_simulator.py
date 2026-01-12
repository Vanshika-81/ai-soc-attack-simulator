
import random
from datetime import datetime

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

def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

TARGET_IP = "192.168.1.10"

def generate_normal_traffic():
    return TrafficEvent(
        random_ip(), TARGET_IP, 80,
        random.randint(10, 40),
        "normal"
    )

def generate_ddos_traffic(intensity):
    return TrafficEvent(
        random_ip(), TARGET_IP, 80,
        int(random.randint(300, 600) * intensity),
        "ddos"
    )

def generate_bruteforce_traffic(intensity):
    return TrafficEvent(
        "10.0.0.5", TARGET_IP, 22,
        int(random.randint(40, 80) * intensity),
        "bruteforce"
    )

def generate_portscan_traffic():
    return TrafficEvent(
        "10.0.0.9", TARGET_IP,
        random.randint(1, 1024),
        random.randint(5, 15),
        "portscan"
    )
