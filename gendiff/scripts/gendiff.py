#!/usr/bin/env python3

from gendiff.gendiff import generate_diff
from gendiff.parser import parseargs
import sys


def main():
    options = parseargs(sys.argv[1:])
    args = vars(options).values()
    print(generate_diff(*args))


if __name__ == '__main__':
    main()
