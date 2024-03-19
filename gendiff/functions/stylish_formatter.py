import json


def stylish(dict_diff: dict):
    #return dict_diff
    return make_string(add_depth(dict_diff))


def make_string(tree):
    spaces_per_level = 4
    shift_left = 2
    result_string = ""
    for nod in tree:
        shift = ' ' * (nod['depth'] * spaces_per_level - shift_left)
        if nod["status"] == 'updated':
            result_string += f"{shift}- {nod['name']}: {nod['old_value']}\n"
            result_string += f"{shift}+ {nod['name']}: {nod['new_value']}\n"
        if nod["status"] == 'same':
            result_string += f"{shift}  {nod['name']}: {nod['value']}\n"
        if nod["status"] == 'added':
            result_string += f"{shift}+ {nod['name']}: {nod['value']}\n"
        if nod["status"] == 'removed':
            result_string += f"{shift}- {nod['name']}: {nod['value']}\n"
        if nod["status"] == 'updated_dict':
            result_string += f"{shift}  {nod['name']}: \n{make_string(nod['children'])}"
    return result_string


def add_depth(tree):
    def walk_(nod, depth):
        for child in nod:
            new_depth = depth + 1
            child.update({"depth": depth})
            if "children" in child:
                walk_(child.get("children"), new_depth)
        return tree
    return walk_(tree, 0)


"""
def make_string(tree):
    result_string = ""
    for nod in tree:
        if nod["status"] == 'updated':
            result_string += f"- {nod['name']}: {nod['old_value']}"
            new_dict[f"+ {nod['name']}"] = nod["new_value"]
        if nod["status"] == 'same':
            new_dict[f"**{nod['name']}"] = nod["value"]
        if nod["status"] == 'added':
            new_dict[f"+ {nod['name']}"] = nod["value"]
        if nod["status"] == 'removed':
            new_dict[f"- {nod['name']}"] = nod["value"]
        if nod["status"] == 'updated_dict':
            new_dict[f"**{nod['name']}"] = add_prefix_make_dict(nod["children"])
    return new_dict
def make_string(tree):
    spaces_per_level = 4
    shift_left = 2
    result_string = ""
    for nod in tree:
        shift = ' ' * (nod['depth'] * spaces_per_level - shift_left)
        if nod["status"] == 'updated':
            result_string += f"{shift}- {nod['name']}: {nod['old_value']}\n"
            result_string += f"{shift}+ {nod['name']}: {nod['new_value']}\n"
        if nod["status"] == 'same':
            result_string += f"{shift}  {nod['name']}: {nod['value']}\n"
        if nod["status"] == 'added':
            result_string += f"{shift}+ {nod['name']}: {nod['value']}\n"
        if nod["status"] == 'removed':
            result_string += f"{shift}- {nod['name']}: {nod['value']}\n"
        if nod["status"] == 'updated_dict':
            result_string += f"{shift}  {nod['name']}: \n{make_string(nod['children'])}"
    return result_string 
"""