#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys
import signal


def signal_handler(signal, frame):
    """signal handler to print stats before exiting"""
    print_stats()
    sys.exit(0)


def parse_line(line):
    """parse line and return status code and file size"""
    try:
        data = list(line.split())
        status_code = data[-2]
        file_size = int(data[-1])
        return status_code, file_size
    except ValueError:
        return None, None
    except IndexError:
        return None, None


def print_stats():
    """print stats"""
    print(f"Total file size: {total_size}")
    for status_code, count in counts.items():
        if count > 0:
            print(f"{status_code}: {count}")


# Set up a signal handler to exit when Ctrl+C is pressed
signal.signal(signal.SIGINT, signal_handler)

# Initialize total size of files and a dictionary to count each status code
total_size = 0
codes = ("200", "301", "400", "401", "403", "404", "405", "500")
counts = {status_code: 0 for status_code in codes}

i = 0
for line in sys.stdin:
    status_code, file_size = parse_line(line)
    if status_code is not None:
        if status_code in codes:
            counts[status_code] += 1
        total_size += file_size
    i += 1
    if i % 10 == 0:
        print_stats()
