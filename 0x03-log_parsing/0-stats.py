#!/usr/bin/python3
import sys
import signal
import re

# initialize variables
total_size = 0
status_code_counts = {
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

# compile regex pattern
log_pattern = re.compile(
    r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')


def print_statistics():
    """Print the collected statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def process_line(line):
    """Process a single line of input"""
    global total_size, status_code_counts, line_counter

    match = log_pattern.match(line)
    if not match:
        return

    try:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
    except (ValueError, IndexError):
        return

    if status_code in status_code_counts:
        status_code_counts[status_code] += 1
    total_size += file_size
    line_counter += 1


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        process_line(line.strip())
        if line_counter % 10 == 0:
            print_statistics()
        # Print statistics at the end of the input or if no lines were
        # processed
    if line_counter % 10 != 0:
        print_statistics()
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
