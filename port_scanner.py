import socket
import datetime

def scan_ports(host):
    print(f"\n[+] Scanning target: {host}")
    print(f"[+] Scan started at: {datetime.datetime.now()}\n")
    open_ports = []

    for port in range(1, 1025):  # Scanning common ports (1-1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)  # Timeout for unresponsive ports
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[*] Port {port} is OPEN")
            open_ports.append(port)
        sock.close()

    if not open_ports:
        print("\n[!] No open ports found.")
    else:
        print(f"\n[+] Open ports: {open_ports}")

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    scan_ports(target)
