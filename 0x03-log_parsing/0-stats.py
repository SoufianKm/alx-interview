#!/usr/bin/python3
""" A script that generates random HTTP request logs. """
import sys
import signal


# Initialize total file size and status code counts
total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_statistics(stats, total_size):
    """
    Print the total file size and the number of lines per status code.
    """
    print("Total file size: {}".format(total_size))
    for status_code in sorted(stats.keys()):
        if stats[status_code] > 0:
            print("{}: {}".format(status_code, stats[status_code]))


def signal_handler(sig, frame):
    """
    Signal handler to print statistics when a keyboard
    interruption (CTRL + C) occurs.
    """
    print_statistics(status_counts, total_size)
    sys.exit(0)


if __name__ == "__main__":
    # Set up signal handler for keyboard interruption
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()

            # Process status code
            try:
                status_code = data[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except IndexError:
                # If there's an issue with accessing data
                # elements, skip this line
                continue

            # Process file size
            try:
                total_size += int(data[-1])
            except (IndexError, ValueError):
                # If there's an issue with converting
                # the file size, skip this part
                continue

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(status_counts, total_size)

        # Print final statistics
        print_statistics(status_counts, total_size)

    except KeyboardInterrupt:
        print_statistics(status_counts, total_size)
        raise
