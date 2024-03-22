def stylish(dict_diff: dict):
    return "\n".join(make_string(add_depth(dict_diff)).replace
                     ('\n\n', '\n').split("\n")[:-1])


def make_string(tree):
    result_string = ""
    prev_depth = "start"
    for nod in tree:
        spaces_per_level = 4
        shift_left = 2
        depth = nod['depth']
        status = nod["status"]
        name = nod['name']
        shift_before = ' ' * (depth * spaces_per_level - shift_left)
        shift_after = ' ' * ((depth - 1) * spaces_per_level)
        if depth != prev_depth:
            result_string += "{\n"
        if depth == prev_depth and result_string.endswith("}\n"):
            result_string = \
                "\n".join(result_string.split("\n")[:-2]) + \
                "\n"  # delete bracket line between same depth nods
        if status == 'updated':
            result_string += \
                f"{shift_before}- {name}: {to_str(nod['old_value'])}\n"
            result_string += \
                f"{shift_before}+ {name}: {to_str(nod['new_value'])}\n"
        if status == 'same':
            result_string += \
                f"{shift_before}  {name}: {to_str(nod['value'])}\n"
        if status == 'added':
            result_string += f"{shift_before}+ {name}: {to_str(nod['value'])}\n"
        if status == 'removed':
            result_string += \
                f"{shift_before}- {name}: {to_str(nod['value'])}\n"
        if status == 'nested':
            result_string += \
                f"{shift_before}  {name}: {make_string(nod['children'])}\n"
        if ("children" in nod and status != 'nested'
                and (status != 'updated'
                     or (status == "updated"
                         and isinstance(nod['new_value'], dict)))):
            result_string = (result_string.split(name)[0]
                             + f"{name}: {make_string(nod['children'])}\n")
        if ("children" in nod and "old_value" in nod
                and isinstance(nod["old_value"], dict)):
            result_string = (result_string.split(name)[0]
                             + f"{name}: {make_string(nod['children'])}\n")
            result_string += \
                f"{shift_before}+ {name}: {to_str(nod['new_value'])}\n"
        result_string += shift_after + "}\n"
        prev_depth = depth
    return result_string


def add_depth(tree):
    def walk_(nod, depth):
        for child in nod:
            new_depth = depth + 1
            child.update({"depth": depth})
            if "children" in child:
                walk_(child.get("children"), new_depth)
        return tree

    return walk_(tree, 1)


def to_str(value):
    if value is False:
        return "false"
    if value is True:
        return "true"
    if value is None:
        return "null"
    if value == 0:
        return "0"
    if value == "0":
        return value
    else:
        return value
