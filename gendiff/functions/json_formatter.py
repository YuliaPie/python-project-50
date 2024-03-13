import json


def to_json(dict_diff):
    return json.dumps(delete_asterisk(dict_diff), indent=2)


def delete_asterisk(dict_diff):
    keys = dict_diff.keys()
    dict_no_aster = {}
    for key in keys:
        value = dict_diff[key]
        if isinstance(value, dict):
            dict_no_aster[key.replace('*', " ")] = delete_asterisk(value)
        else:
            dict_no_aster[key.replace('*', " ")] = value
    return dict_no_aster
