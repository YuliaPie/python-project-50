#!/usr/bin/env python
from gendiff.parser import parser
from gendiff.generate_diff import generate_diff


def main():
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
