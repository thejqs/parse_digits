#!usr/bin/env python3

"""
A test suite for our parser, testing granular function output,
cross-file return structure and sharing, and a
range of inputs.

"""

# standard library imports
import unittest
import sys

sys.path.append('/home/thejqs/Development/projects_2016/parse_digits/')

# project imports
from parser import parse_digits as pd
from parser import run_parse_digits as rpd

lst = [1, 129, 129, 7, 2, 6, 2398562906, 9]
# this test file contains 1000 numbers
path = 'data/test_data.txt'
# this one contains 9999 numbers
path2 = 'data/numbers.txt'

class DigitParserTextCase(unittest.TestCase):
    def test_parse_digits_mode(self):
        self.assertEqual(pd.find_mode(lst)[0], 129)

    def test_parse_digits_mode_frequency(self):
        self.assertEqual(pd.find_mode(lst)[1], 2)

    def test_parse_digits_median(self):
        self.assertEqual(pd.find_median(lst), 8.0)

    def test_parse_digits_length(self):
        self.assertEqual(pd.find_length(lst), 8)

    def test_parse_digits_max(self):
        self.assertEqual(pd.find_largest(lst), 2398562906)

    def test_parse_digits_min(self):
        self.assertEqual(pd.find_smallest(lst), 1)

    def test_parser_return(self):
        self.assertIn(48, rpd.run_parser(path))
        self.assertIn(1, rpd.run_parser(path))
        self.assertIn(100, rpd.run_parser(path))
        self.assertIn(13, rpd.run_parser(path))
        self.assertIn(19, rpd.run_parser(path))

    def test_with_larger_data_set(self):
        self.assertIn(499, rpd.run_parser(path2))
        self.assertIn(1, rpd.run_parser(path2))
        self.assertIn(1000, rpd.run_parser(path2))
        self.assertIn(205, rpd.run_parser(path2))
        self.assertIn(21, rpd.run_parser(path2))
