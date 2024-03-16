def plain(dict_diff: dict):
    return form_string(add_path(dict_diff))


def add_path(tree):
    def walk_(nod, path, new_tree=[]):
        for child in nod:
            new_path = f"{path}.{child['name']}"
            child.update({"path": path})
            new_tree.append(child)
            if "children" in child:
                walk_(child.get("children"), new_path)
        return new_tree
    return walk_(tree, "")


def form_string(nod):
    strings = []
    for child in nod:
        property = delete_starting_dot(f"{child['path']}.{child['name']}")
        status = child['status']
        if status != "updated_dict" and status != "same":
            string = f"Property '{property}' was {status}"
            if status == "added":
                string += f" with value: {uniform_value(child["value"])}"
            if status == "updated":
                string += (f". From {uniform_value(child["old_value"])} to "
                           f"{uniform_value(child["new_value"])}")
            strings.append(string)
    return "\n".join(strings)


def delete_starting_dot(source_string):
    if source_string[0] == ".":
        return delete_starting_dot(source_string[1::])
    else:
        return source_string


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
