#!/usr/bin/env python
from gendiff.functions.comparator import generate_diff
from gendiff.functions.parser import parser

def main():
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
