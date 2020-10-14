#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = '''Tracy Dewitt,
https://docs.python.org/3/library/logging.html,
https://youtu.be/-ARI4Cz-awo,
https://youtu.be/jxmzY9soFXg,

'''

import sys
import time
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
    # Your code here
    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    return


def create_parser():
    # Your code here
    return


def signal_handler(sig_num, frame):
    # Your code here
    return


def main(args):
    # Your code here
    return


if __name__ == '__main__':
    main(sys.argv[1:])
