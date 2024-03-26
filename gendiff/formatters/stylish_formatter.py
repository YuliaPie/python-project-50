from gendiff.comparison_tree import compare_dicts


def stylish(dict_diff: dict):
    return make_string(dict_diff)


def make_string(tree, depth=1):
    def walk(nod, depth, result=""):
        spaces_per_level = 4
        shift_left = 2
        for child in nod:
            indent = (depth * spaces_per_level - shift_left) * " "
            new_depth = depth + 1
            result += "\n"
            if child['status'] == 'removed':
                result += (indent + "- " + child["name"]
                           + ": " + str(to_str(child["value"], new_depth)))
            elif child['status'] == 'added':
                result += (indent + "+ " + child["name"]
                           + ": " + str(to_str(child["value"], new_depth)))
            elif child['status'] == 'nested':
                result += (indent + "  " + child["name"]
                           + ": " + walk(child["children"],
                                         new_depth, result=""))
            elif child['status'] == 'updated':
                result += (indent + "- " + child["name"]
                           + ": " + str(to_str(child["old_value"],
                                               new_depth)) + "\n")
                result += (indent + "+ " + child["name"]
                           + ": " + str(to_str(child["new_value"], new_depth)))
            elif child['status'] == 'same':
                result += (indent + "  " + child["name"]
                           + ": " + str(to_str(child["value"], new_depth)))
        return "{" + result + "\n" + spaces_per_level * (depth - 1) * " " + "}"
    return walk(tree, depth, "")


def to_str(value, depth=0):
    if isinstance(value, dict):
        return make_string(compare_dicts(value, value), depth)
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
