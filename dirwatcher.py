#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = '''Tracy Dewitt,
https://docs.python.org/3/library/logging.html,
https://youtu.be/-ARI4Cz-awo,
https://youtu.be/jxmzY9soFXg,
Babynames Assessment,
Word count Assessment,

'''

import sys
import signal
import time
import argparse
import os
import logging


# Level(#'val)           When it’s used

# DEBUG(10)          Detailed information, typically of interest only when
#                    diagnosing problems.

# INFO(20)           Confirmation that things are working as expected.

# WARNING(30)        An indication that something unexpected happened, or
#                    indicative of some problem in the near future
#                    (e.g. ‘disk space low’).
#                    The software is still working as expected.

# ERROR(40)          Due to a more serious problem, the software has not been
#                    able to perform some function.

# CRITICAL(50)       A serious error, indicating that the program itself may be 
#                    unable to continue running.

exit_flag = False


global_dict = {}


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('file.log')
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def search_for_magic(filename, start_line, magic_string, path):

    with open(f'{path} {filename}') as f:
        for n, s in enumerate(f):
            if s.find(magic_string) != -1:
                print(f'{filename}/{n}')

    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    return


def create_parser():
    parser = argparse.ArgumentParser(
        description="Looking for changing files in directory.")

    parser.add_argument(
        '-e', '--ext', help='extension input')

    parser.add_argument(
        '-d', '--dir', help='directory input')

    parser.add_argument(
        '-i', '--int', default=1, help='polling interval period of time\
                        between the end of the timeout period')

    parser.add_argument(
        '-t', '--txt', help='magic search')
    return


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other signals can be mapped here as well (SIGHUP?)
    Basically, it just sets a global flag, and main() will exit its loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    global exit_flag
    # log the associated signal name
        logger.warn('Received ' + signal.Signals(sig_num).name)
    exit_flag = True




def main(args):
    # Hook into these two signals from the OS
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.

    while not exit_flag:
        try:
            # call my directory watching function
            pass
        except Exception as e:
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            pass

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        # time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start
    return


if __name__ == '__main__':
    main(sys.argv[1:])
