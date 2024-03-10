import json
import yaml

# import argparse

"""
parser = argparse.ArgumentParser(description="Contains functions")
parser.add_argument("-F", "--formatter", default="stylish")
args = parser.parse_args()
"""


def generate_diff(path1, path2):
    dict1 = convert_to_dict(path1)
    dict2 = convert_to_dict(path2)
    dict_diff = compare_dicts(dict1, dict2)
    return stylish(dict_diff)


def compare_dicts(dict1, dict2):
    keys = list(set(dict1.keys()) | set(dict2.keys()))
    keys.sort()
    dict_diff = {}
    for key in keys:
        value_1 = dict1.get(key, "No_key")
        value_2 = dict2.get(key, "No_key")
        if value_1 == value_2:
            dict_diff[f"**{key}"] = value_1
        if value_1 == "No_key":
            dict_diff[f"+ {key}"] = value_2
        if value_2 == "No_key":
            dict_diff[f"- {key}"] = value_1
        if (not value_1 == "No_key" and not value_2 == "No_key"
                and value_1 != value_2):
            if isinstance(value_1, dict) and isinstance(value_2, dict):
                dict_diff[f"**{key}"] = compare_dicts(value_1, value_2)
            else:
                dict_diff[f"- {key}"] = value_1
                dict_diff[f"+ {key}"] = value_2
    return dict_diff


def get_extension(path_to_file):
    return path_to_file.split(".")[-1]


def convert_to_dict(file):
    extension = get_extension(file)
    if extension == "yml" or extension == "yaml":
        file = open(file)
        return yaml.load(file, Loader=yaml.Loader)
    if extension == "json":
        return json.load(open(file))


def stylish(dict_diff: dict):
    pretty_dict_diff = json.dumps(dict_diff, indent=4)
    diff_str = str(pretty_dict_diff)
    diff_str = diff_str.replace('"', "")
    diff_str = diff_str.replace(',\n', "\n")
    diff_str = move_left(diff_str)
    diff_str = diff_str.replace('*', " ")
    return diff_str


def move_left(styled_string):
    lines = styled_string.split("\n")
    new_lines = []
    for line in lines:
        if "**" in line or "+ " in line or "- " in line:
            line = line[2::]
        new_lines.append(line)
    return "\n".join(new_lines)
