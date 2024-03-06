#!/usr/bin/env python
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration "
                                                 "files and shows a "
                                                 "difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def generate_diff(path1, path2):
    file_path1 = json.load(open(path1))
    file_path2 = json.load(open(path2))
    keys = list(set(file_path1.keys()) | set(file_path2.keys()))
    keys.sort()
    dict_diff = {}
    for key in keys:
        value_1 = file_path1.get(key, "No_key")
        value_2 = file_path2.get(key, "No_key")
        if value_1 == value_2:
            dict_diff[f"  {key}"] = value_1
        if value_1 == "No_key":
            dict_diff[f"+ {key}"] = value_2
        if value_2 == "No_key":
            dict_diff[f"- {key}"] = value_1
        if (not value_1 == "No_key" and not value_2 == "No_key"
                and value_1 != value_2):
            dict_diff[f"- {key}"] = value_1
            dict_diff[f"+ {key}"] = value_2
    pretty_dict_diff = json.dumps(dict_diff, indent=2)
    diff_str = str(pretty_dict_diff)
    diff_str = diff_str.replace('"', "")
    diff_str = diff_str.replace(',\n', "\n")
    return diff_str


if __name__ == '__main__':
    main()
