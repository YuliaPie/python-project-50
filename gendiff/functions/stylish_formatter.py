import json


def stylish(dict_diff: dict):
    return json.dumps(add_prefix_make_dict(dict_diff), indent=4)
    return json.dumps(dict_diff, indent=4)


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
            new_dict[f"- {nod["name"]}"] = add_prefix_make_dict(nod["children"])
    return new_dict

"""

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
    
    
    pretty_dict_diff = json.dumps(add_prefix(dict_diff), indent=4)
    diff_str = str(pretty_dict_diff)
    diff_str = diff_str.replace('"', "")
    diff_str = diff_str.replace(',\n', "\n")
    diff_str = move_left(diff_str)
    diff_str = diff_str.replace('*', " ")
    return diff_str

def add_prefix(dict_diff):
    new_dict ={}
    keys = dict_diff.keys()
    for key in keys:
        if dict_diff[key]["status"] == 'same':
            new_dict[f"**{key}"] = dict_diff[key]["value"]
        if dict_diff[key]["status"] == 'added':
            new_dict[f"+ {key}"] = dict_diff[key]["value"]
        if dict_diff[key]["status"] == 'removed':
            new_dict[f"- {key}"] = dict_diff[key]["value"]
        if dict_diff[key]["status"] == 'updated_dict':
            new_dict[f"**{key}"] = add_prefix(dict_diff[key]["value"])
        if dict_diff[key]["status"] == 'updated':
            new_dict[f"- {key}"] = dict_diff[key]["old_value"]
            new_dict[f"+ {key}"] = dict_diff[key]["new_value"]
    return new_dict
"""

def move_left(styled_string):
    lines = styled_string.split("\n")
    new_lines = []
    for line in lines:
        if "**" in line or "+ " in line or "- " in line:
            line = line[2::]
        new_lines.append(line)
    return "\n".join(new_lines)

