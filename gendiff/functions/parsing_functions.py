import json
import yaml


def get_data_and_extension(path_to_file):
    data = open(path_to_file)
    extension = path_to_file.split(".")[-1]
    return data, extension


def parse(data, extension):
    if extension == "yml" or extension == "yaml":
        return yaml.load(data, Loader=yaml.Loader)
    if extension == "json":
        return json.load(data)
