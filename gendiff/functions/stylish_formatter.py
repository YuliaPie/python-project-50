import json


def stylish(dict_diff: dict):
    return make_string(add_prefix_make_dict(dict_diff))


def add_prefix_make_dict(tree):
    new_dict = {}
    for nod in tree:
        if nod["status"] == 'updated':
            new_dict[f"- {nod["name"]}"] = nod["old_value"]
            new_dict[f"+ {nod["name"]}"] = nod["new_value"]
        if nod["status"] == 'same':
            new_dict[f"**{nod["name"]}"] = nod["value"]
        if nod["status"] == 'added':
            new_dict[f"+ {nod["name"]}"] = nod["value"]
        if nod["status"] == 'removed':
            new_dict[f"- {nod["name"]}"] = nod["value"]
        if nod["status"] == 'updated_dict':
            new_dict[f"**{nod["name"]}"] = add_prefix_make_dict(nod["children"])
    return new_dict


def make_string(dict_diff):
    pretty_dict_diff = json.dumps(dict_diff, indent=4)
    diff_str = str(pretty_dict_diff)
    diff_str = diff_str.replace('"', "")
    diff_str = diff_str.replace(',\n', "\n")
    diff_str = move_left(diff_str)
    diff_str = diff_str.replace('*', " ")
    return diff_str


def move_left(styled_string):
    lines = styled_string.split("\n")
    new_lines = []
    for line in lines:
        if "**" in line or "+ " in line or "- " in line:
            line = line[2::]
        new_lines.append(line)
    return "\n".join(new_lines)
