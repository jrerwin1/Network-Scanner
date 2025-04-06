# --------------------------------------------
# Author: Joshua Erwin
# Project: Network Scanner & Port Monitor
# Description: Scans a subnet for live hosts and common open ports.
# Date: April 2025
# --------------------------------------------

import socket
import ipaddress
import subprocess
from datetime import datetime

# Define subnet and common ports
subnet = "192.168.1.0/24"
ports_to_check = [22, 80, 443, 3389, 445]
report_file = f"scan_report_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"

def is_host_up(ip):
    try:
        output = subprocess.check_output(['ping', '-n', '1', '-w', '500', str(ip)], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((str(ip), port))
            return result == 0
    except:
        return False

def log(msg):
    print(msg)
    with open(report_file, 'a') as f:
        f.write(msg + "\n")

def scan_network():
    log(f"Network Scan Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log("----------------------------------------------------\n")
    
    for ip in ipaddress.IPv4Network(subnet):
        if is_host_up(ip):
            log(f"[+] Host up: {ip}")
            for port in ports_to_check:
                if scan_port(ip, port):
                    log(f"    - Port {port} open")
        else:
            print(f"[-] No response from {ip}")
    log("\nScan complete.")

if __name__ == "__main__":
    scan_network()
