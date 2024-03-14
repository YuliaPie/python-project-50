def plain(dict_diff: dict):
    # return dict_diff
    return add_parents(dict_diff)
    # return form_string(add_parents(dict_diff))


def add_parents(dict_diff):
    keys = dict_diff.keys()
    for key in keys:
        if isinstance(dict_diff[key], dict):
            if "parent" in dict_diff and isinstance(dict_diff[key]["value"], dict):
                dict_diff[key]["value"]["parent"] = [dict_diff[key].get("parent","")] + [key]
            if "parent" not in dict_diff:
                dict_diff[key]["parent"] = [key]
            if dict_diff[key].get("value") and isinstance(dict_diff[key]["value"], dict):
                add_parents(dict_diff[key]["value"])
    return dict_diff


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
