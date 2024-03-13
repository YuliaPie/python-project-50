from gendiff.functions.plain_formatter import plain
from gendiff.functions.stylish_formatter import stylish
from gendiff.functions.json_formatter import to_json

def select_formatter(dict, format_name):
    if format_name == "stylish":
        return stylish(dict)
    if format_name == "plain":
        return plain(dict)
    if format_name == "json":
        return to_json(dict)