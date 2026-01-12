# ai-soc-attack-simulator
# AI-Driven SOC Resilience Monitor

An AI-driven Security Operations Center (SOC) dashboard that simulates real-time network traffic, cyberattacks, and SOC response behavior.  
The system helps visualize how resilient a SOC is under different types of network traffic and attack scenarios.

---

## 📌 Project Objective

To **simulate normal and malicious network traffic**, detect cyberattacks, and evaluate the **resilience of a SOC** using a live dashboard.

The project demonstrates:
- Real-time traffic generation
- Attack simulation (Port Scan, Brute Force, DDoS, Mixed)
- Detection and alerting
- Dynamic resilience scoring

---

## 🧠 Key Features

### ✅ Traffic Simulation
- **Normal Traffic**
- **Port Scan**
- **Brute Force**
- **DDoS**
- **Mixed Traffic** (random mix of all attack types)

Traffic is generated dynamically by the backend and streamed to the frontend every second.

---

### ✅ Real-Time Dashboard
- Live traffic table
- Dual-line chart (Normal vs Attack traffic rate)
- Interactive attack simulator buttons
- Live metric cards

---

### ✅ Metrics Displayed
- **Normal Traffic Count**
- **Attack Traffic Count**
- **Alert Flags**
- **Resilience Score**

---

## 📊 Resilience Score Logic (Important)

The **Resilience Score represents how well the SOC is handling attacks**.

### How it works:
- The score **starts at 100%**
- Each detected alert slightly reduces the score
- It is calculated as:
Resilience Score = (1 - Alerts / Total Events) × 100

### Why this is correct:
- Starts at **100%**
- Decreases **gradually**, not instantly
- Never goes below 0%
- Mimics real-world SOC resilience evaluation

---

## 🧩 System Architecture

Frontend (HTML + CSS + JavaScript)
|
| Fetch API (HTTP, JSON)
|
Backend (Flask + Python)

---

## 🗂️ Project Structure

AI-SOC-ATTACK-SIMULATOR/
│
├── backend/
│ ├── app.py # Flask backend server
│ ├── detection_engine.py
│ ├── traffic_simulator.py
│ └── requirements.txt
│
├── frontend/
│ └── dashboard.html # Main SOC dashboard
│
├── docs/
│
└── README.md

---

## 🚀 How to Run the Project

### 1️⃣ Start Backend

```bash
cd backend
python app.py

Backend runs at:

http://127.0.0.1:5000
2️⃣ Start Frontend
cd frontend
python -m http.server 3000


Open in browser:

http://127.0.0.1:3000/dashboard.html

🎮 How to Use

Click Normal Traffic → Only normal events

Click Port Scan / Brute Force / DDoS → Specific attack simulation

Click Mixed Traffic → Random mix of all traffic types

Watch metrics, chart, alerts, and resilience score update live

🛠️ Technologies Used

Frontend: HTML, CSS, JavaScript, Chart.js

Backend: Python, Flask, Flask-CORS

Communication: REST APIs (Fetch)

🧪 Educational Value

This project helps understand:

SOC monitoring

Attack detection logic

Incident response visualization

Real-time systems

Cybersecurity simulation concepts

📌 Conclusion

The AI-Driven SOC Resilience Monitor demonstrates how simulated cyberattacks impact network behavior and how SOC effectiveness can be evaluated visually in real time.