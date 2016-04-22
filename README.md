#A parser! For integers!

It's an exciting time. You have files upon files of of what you presume are integers, but you have no good way to get basic analysis of them. We can help.

Snakes might not normally be your friends, but **consider Python**. Perhaps not the fastest languages, perhaps not the new hotness, but it's perfect for something like this. This is written in Python 3.4.

With a pair of simple, tested scripts running together in unison and a couple small modifications, you can quickly see: 

- the largest and smallest values
- the median
- the most-common value and how frequently it occurs
- and the total number of integers analyzed to do all that. 

Simply clone this repo into a project directory of your own, change a couple environment settings, and **all this can be yours**.

After you've cloned the repo, a couple things will help you out. In the `parser/run_parse_digits.py` file, simply replace my sample in `sys.path.append()` with your own project path. Then do the same in the `tests/test_parse_digits.py` file. Those two settings will help you run the tests and diagnose issues should anything untoward happen while running the scripts. Tests can be run from the command line while in the top-level directory with `python -m unittest discover -s tests`.

Meantime, just add in your own file paths and get to analyzing.

The two main parser scripts can be run together or separately. Together and you get some easy-to-read output. Like this:

```python
>>> from parser import run_parse_digits as rpd
>>> rpd.run_parser('data/test_data.txt')

Of 1000 integers:
           	100 was the highest,
           	1 was the lowest,
           	13 occurred the most times with 19,
           	and the median was 48.0.
This script took 0:00:00.004898 to run
```

But it's fine to import `parse_digits` from the `parser` directory and `python parse_digits(your_filepath_here)`. In a case like that, you get back a structured collection, `SummaryDigits`, which is a `namedtuple` and accessible by position or keyword argument. You'll find what you need for either or both inside the file itself. That output looks like this:

```python
>>> from parser import parse_digits as pd
>>> pd.parse_digits('data/test_data.txt')
SummaryDigits(length=1000, maximum=100, minimum=1, mode_value=13, mode_occurrences=19, median=48.0) 
```

So. Good deal. You get a parser for integer files. I feel good about myself. Fair trade all around.

**Now get parsing. Don't make me tell you again.**
