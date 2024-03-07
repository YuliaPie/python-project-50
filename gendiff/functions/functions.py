import json
import yaml


def run(arg1, arg2):
    print(generate_diff(arg1, arg2))
    return (generate_diff(arg1, arg2))


def get_extension(path_to_file):
    return path_to_file.split(".")[-1]


def convert_to_dict(file):
    extension = get_extension(file)
    if extension == "yml" or extension == "yaml":
        file = open(file)
        return yaml.load(file, Loader=yaml.Loader)
    if extension == "json":
        return json.load(open(file))


def make_pretty_str(dict):
    pretty_dict_diff = json.dumps(dict, indent=2)
    diff_str = str(pretty_dict_diff)
    diff_str = diff_str.replace('"', "")
    diff_str = diff_str.replace(',\n', "\n")
    return diff_str


def generate_diff(path1, path2):
    file_path1 = convert_to_dict(path1)
    file_path2 = convert_to_dict(path2)
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
    return make_pretty_str(dict_diff)
