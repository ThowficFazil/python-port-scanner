# python-port-scanner

# 🔍 Python Port Scanner

A simple Python-based network scanner that checks for open ports on a target host.  
This tool is designed for **educational and cybersecurity learning purposes**.

---

## **Features**
- Scans ports **1–1024** (common ports).
- Displays **open ports** in real-time.
- Lightweight and easy to use with **no external libraries**.

---

## **Installation**
1. **Clone this repository:**
   ```bash
   git clone https://github.com/<your-username>/python-port-scanner.git
   ```
2. **Navigate to the folder:**
   ```bash
   cd python-port-scanner
   ```
3. **Run the script:**
   ```bash
   python port_scanner.py
   ```

---

## **Usage Example**
```
Enter target IP or domain: scanme.nmap.org

[+] Scanning target: scanme.nmap.org
[*] Port 22 is OPEN
[*] Port 80 is OPEN
[*] Port 443 is OPEN

[+] Open ports: [22, 80, 443]
```

---

## **Code Explanation**
- **`socket` module** – Used to create network connections.
- **`connect_ex()`** – Checks if a port is open (returns 0 if open).
- **`range(1, 1025)`** – Scans the first 1024 ports.

---

## **Future Enhancements**
- Add multi-threaded scanning for faster results.
- Include service detection (e.g., HTTP, FTP).
- Export results to a `.txt` file.

---

## **Disclaimer**
This tool is intended **for educational purposes only**.  
Do not use it on any system or network without **explicit permission**.

---

## **Author**
**Thowfic Ibrahim Fazil**  
Cybersecurity & Digital Forensics Enthusiast
