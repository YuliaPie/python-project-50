def plain(dict_diff: dict):
    return form_string(add_status_parents(dict_diff))


def add_status_parents(dict_diff):
    new_dict = {}
    keys = dict_diff.keys()
    for key in keys:
        value = dict_diff.get(key)
        new_key = f"{dict_diff.get("parent", "")}.{key[2::]}"
        if "- " in key:
            new_dict[new_key] = {'value': value, 'status': 'removed'}
        if "+ " in key:
            if new_key in new_dict:
                new_dict[new_key].update({'new_value': value,
                                          'status': 'updated'})
            else:
                new_dict[new_key] = {'value': value, 'status': 'added'}
        if "**" in key and isinstance(value, dict):
            value.update({'parent': new_key})
            new_dict.update(add_status_parents(value))
    return new_dict


def form_string(dict_diff: dict):
    strings = []
    for k, v in dict_diff.items():
        property = k[1::]
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
