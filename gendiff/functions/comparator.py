import json
import yaml
from gendiff.functions.form_selector import select_formatter
from gendiff.functions.comparison_tree import compare_dicts


def generate_diff(path_to_file1, path_to_file2, format_name="stylish"):
    dict1 = get_dict(*get_data_and_extension(path_to_file1))
    dict2 = get_dict(*get_data_and_extension(path_to_file2))
    dict_diff = compare_dicts(dict1, dict2)
    return select_formatter(dict_diff, format_name)


def get_data_and_extension(path_to_file):
    data = open(path_to_file)
    extension = path_to_file.split(".")[-1]
    return data, extension


def get_dict(data, extension):
    if extension == "yml" or extension == "yaml":
        return yaml.load(data, Loader=yaml.Loader)
    if extension == "json":
        return json.load(data)
