#!usr/bin/env python3

"""
analyzes a text file containing an unknown number of integers,
returning minimum value, maximum value, total number
processed and the mode. might even throw in median just
for fun.

args:
a path to the file to analyze

returns:
a namedtuple structured thus:
[0] number of integers processed
[1] largest number
[2] smallest number
[3] the most frequently occurring value
[4] the number of occurrences
[5] the median value in the list
"""

from collections import Counter
from collections import namedtuple

def find_median(lst):
    """
    finds or calculates the median value in
    a list of integers.

    args:
    a list of integers

    returns:
    the median value
    """
    # might be sorted already, but let's not take any chances
    sorted_list = sorted(lst)
    len_lst = len(sorted_list)
    if len_lst < 1:
        return 'You are a silly person with an empty list'
    idx = (len_lst - 1) // 2
    # for a list with an odd number of values,
    # we can just find the middle one
    if len_lst % 2:
        return sorted_list[idx]
    # otherwise we can calculate a middle ourselves
    else:
        return (sorted_list[idx] + sorted_list[idx + 1]) / 2.0


def find_length(lst):
    return len(lst)


def find_largest(lst):
    return max(lst)


def find_smallest(lst):
    return min(lst)


def find_mode(lst):
    return Counter(lst).most_common()[0]


def parse_digits(path):
    """
    a parser for a file object containing an unknown number of  integers separated by spaces

    args:
    a path to a file containing the integers
    """
    with open(path, 'r') as f:
        try:
            results = []
            results += [int(l) for line in f for l in line.split()]
            len_results = find_length(results)
            max_result = find_largest(results)
            min_result = find_smallest(results)
            mode = find_mode(results)
            median = find_median(results)
            SummaryDigits = namedtuple('SummaryDigits', ['length', 'maximum', 'minimum', 'mode_value', 'mode_occurrences', 'median'])
            p = SummaryDigits(len_results, max_result, min_result, mode[0], mode[1], median)
            print(p.length)
            return p
        except TypeError as e:
            return '{}\n\t{}'.format(e,
                                    "Are you sure this is really a file full of integers? Because I'm not")

if __name__ == '__main__':
    parse_digits()
