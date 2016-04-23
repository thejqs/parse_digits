#!usr/bin/env python3

"""
supplies a file path to parse_digits.py and runs the script,
giving as clean, human-readable output the filename,
results and execution time 
"""

# standard library imports
import sys
import datetime

sys.path.append('/home/thejqs/Development/projects_2016/panasas_digits/')

# project imports
from parser import parse_digits as pd

def run_parser(path):
    """
    runs a parser for a file object containing an
    unknown number of integers, outputting the return
    in human-readable format.

    the parser returns a namedtuple structured thus:
    [0] number of integers processed
    [1] largest number
    [2] smallest number
    [3] the most frequently occurring value
    [4] the number of occurrences
    [5] the median value in the list

    or if you're a kwargs type of human:
    [0] = length
    [1] = maximum
    [2] = minimum
    [3] = mode_value
    [4] = mode_occurrences
    [5] = median

    args:
    a path to the file in order to supply that to the parser
    """
    start = datetime.datetime.now()
    parsed_digits = pd.parse_digits(path)
    print("""Of {0} integers:
           \t{1} was the highest,
           \t{2} was the lowest,
           \t{3} occurred the most times with {4},
           \tand the median was {5}.""".format(parsed_digits[0],
                                         parsed_digits[1],
                                         parsed_digits[2],
                                         parsed_digits[3],
                                         parsed_digits[4],
                                         parsed_digits[5]))
    end = datetime.datetime.now()
    print('This script took {} to run'.format(end - start))
    return parsed_digits


if __name__ == '__main__':
    path = '../data/numbers.txt'
    run_parser(path)
