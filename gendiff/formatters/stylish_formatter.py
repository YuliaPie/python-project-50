from gendiff.comparison_tree import compare_dicts
from gendiff.constants import SPACES_PER_LEVEL, SHIFT_LEFT


def stylish(dict_diff: dict):
    return make_string(dict_diff)


def make_string(tree, depth=1):
    def walk(node, depth, result=""):
        for child in node:
            new_depth = depth + 1
            indent = make_indent(depth)
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
        return "{" + result + "\n" + SPACES_PER_LEVEL * (depth - 1) * " " + "}"

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


def make_indent(depth):
    indent = (depth * SPACES_PER_LEVEL - SHIFT_LEFT) * " "
    return indent
