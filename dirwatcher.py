#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = '''Tracy Dewitt,
Manuel Valasco,
Arianna Basha,
Peter Mayor,
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
import datetime


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


def search_for_magic(filename, start_line, magic_string):
    with open(filename) as f:
        line_num_found = []
        for line_num, line_string in enumerate(f):
            if line_num < start_line:
                continue
            file_only = filename.split('/')[1]
            global_dict[file_only] = line_num+1
            if line_string.find(magic_string) != -1:
                line_num_found.append(line_num+1)
        if line_num_found:
            logger.info(f'File Name: {filename}')
            logger.info(f'Found Line #: {line_num_found}')


def watch_directory(path, magic_string, extension, interval):
    file_ls = os.listdir(path)
    for key in list(global_dict):
        if key not in file_ls:
            logger.info(f"File Deleted: {key}")
            global_dict.pop(key)
    for file_name in file_ls:
        if file_name not in global_dict and extension in file_name:
            global_dict[file_name] = 0
            logger.info(f'File Found: {file_name}')
        if extension in file_name:
            search_for_magic(path + '/' + file_name, global_dict[file_name],
                             magic_string)

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

    return parser


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other signals can be mapped here
    as well (SIGHUP?)
    Basically, it just sets a global flag, and main() will exit its loop if
    the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    global exit_flag
    # log the associated signal name
    if signal.Signals(sig_num).name == 'SIGINT':
        logger.warning('Received ' + signal.Signals(sig_num).name)
    exit_flag = True


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    # Hook into these two signals from the OS
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.
    start_up_time = datetime.datetime.now()

    logger.info(f'''

-----------------------------------------------------------------

            Watching: dirwatcher.py
            Start Up: {start_up_time}\n
-----------------------------------------------------------------

''')

    while not exit_flag:
        try:
            # call my directory watching function
            watch_directory(ns.dir, ns.txt, ns.ext, ns.int)
            time.sleep(ns.int)
            pass
        except Exception as e:
            logger.error(e)
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            pass

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        time.sleep(ns.int)
    uptime = datetime.datetime.now() - start_up_time

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start

    logger.info('Good Bye')
    logger.info(f'''

-----------------------------------------------------------------

            Stop: dirwatcher.py
            uptime: {uptime}\n
-----------------------------------------------------------------

''')

    return


if __name__ == '__main__':
    main(sys.argv[1:])
