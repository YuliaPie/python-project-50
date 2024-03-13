def plain(dict_diff: dict):
    return add_parents(dict_diff)
    #return form_string(add_parents(dict_diff))


def add_parents(dict_diff):
    new_dict = {}
    keys = dict_diff.keys()
    for key in keys:
        parent = dict_diff[key].get("parent", "")
        new_key = f"{parent}.{key}"
        if dict_diff[key]["status"] != "updated_dict":
            new_dict[key] = dict_diff[key]
        if dict_diff[key]["status"] == "updated_dict":
            new_dict[key] = dict_diff[key].update({'parent': new_key})
            new_dict.update(add_parents(dict_diff[key]["value"]))
    return new_dict

"""
        parent = dict_diff[key].get("parent", "")
        new_key = f"{parent}.{key}"
        if not isinstance(dict_diff[key]["value"], dict):
            new_dict[new_key] = {'value': dict_diff[key]["value"], 'status': dict_diff[key]["status"]}
        if isinstance(dict_diff[key]["value"], dict):
            dict_diff[key]["value"].update({'parent': new_key})
            new_dict.update(add_parents(dict_diff[key]["value"]))




def form_string(dict_diff: dict):
    strings = []
    for k, v in dict_diff.items():
        property = v['parent'][1::] + k
        status = v['status']
        value = uniform_value(v['value'])
        string = f"Property '{property}' was {status}"
        if status == "added":
            string += f" with value: {value}"
        if status == "updated":
            new_value = uniform_value(v.get('new_value'))
            string += f". From {value} to {new_value}"
        strings.append(string)
    return "\n".join(strings)


def uniform_value(value):
    if value is False:
        return "false"
    if value is True:
        return "true"
    if value is None:
        return "null"
    if isinstance(value, dict):
        return "[complex value]"
    else:
        return f"'{value}'"
"""