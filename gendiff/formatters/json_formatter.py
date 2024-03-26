import json


def to_json(dict_diff):
    return json.dumps(dict_diff, indent=2)
