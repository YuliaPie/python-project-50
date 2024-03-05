#!/usr/bin/env python
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    file_path1 = json.load(open(args.first_file))
    file_path2 = json.load(open(args.second_file))
    diff = generate_diff(file_path1, file_path2)
    print(diff)

def generate_diff(file_path1, file_path2):
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
        if not value_1 == "No_key" and not value_2 == "No_key" and value_1 != value_2:
            dict_diff[f"- {key}"] = value_1
            dict_diff[f"+ {key}"] = value_2
    pretty_dict_diff = json.dumps(dict_diff, indent=2)
    diff_str = str(pretty_dict_diff)
    diff_str = diff_str.replace('"',"")
    return diff_str

if __name__ == '__main__':
    main()
