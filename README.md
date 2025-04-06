# Network Scanner & Port Monitor

This Python script scans a local subnet to identify live hosts and check for open common ports (e.g., SSH, HTTP, HTTPS, RDP). It outputs the results to both the terminal and a timestamped text file.

## Features

- Ping sweep of a given subnet (e.g., 192.168.1.0/24)
- Scans for common open ports: 22, 80, 443, 445, 3389
- Logs output to a `.txt` report with timestamp
- Simple and self-contained — no external libraries required

## Requirements

- Python 3.7+
- Windows OS (uses `ping` command via `subprocess`)

## How to Run

1. Clone the repository or download `network_scanner.py`
2. In the terminal or Anaconda Prompt:
   ```bash
   python network_scanner.py

3. After scanning, a report will be generated as such:
   scan_report_2025-04-06_20-12.txt

