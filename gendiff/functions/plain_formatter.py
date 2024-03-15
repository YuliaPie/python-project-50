def plain(dict_diff: dict):
    return add_path(dict_diff)

def add_path(tree):
    def walk_(nod, path, new_tree = []):
        for child in nod:
            new_path = f"{path}.{child['name']}"
            child.update({"path": path})
            new_tree.append(child)
            if "children" in child:
                walk_(child.get("children"), new_path)
        return new_tree
    return walk_(tree, "")




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
