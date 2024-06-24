#!/usr/bin/python3
"""0-stats.py - script that reads
from stdin and computes metrics"""
import sys
import signal

total_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

line_counter = 0


def print_statistics():
    """print the collected statistics"""
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


def process_line(line):
    """process a single line of input"""
    global total_size, status_code_count, line_counter
    # Expected format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    # <status code> <file size>
    parts = line.split()
    if len(parts) < 9:
        return

    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
    except (ValueError, IndexError):
        return

    if status_code in status_code_count:
        status_code_count[status_code] += 1
    total_size += file_size
    line_counter += 1


def signal_handler(sig, frame):
    """Handle keyboard interuption (CTRL + C)"""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        process_line(line.strip())
        """this code ensures that statistics are printed
        every 10 lines"""
        if line_counter % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
