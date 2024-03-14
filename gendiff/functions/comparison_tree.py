def compare_dicts(dict1, dict2):
    keys = list(set(dict1.keys()) | set(dict2.keys()))
    keys.sort()
    dict_diff = []
    for key in keys:
        if key in dict1 and key in dict2 and dict1[key] == dict2[key]:
            dict_diff.append({"name": key, 'status': 'same'})
        if key not in dict1 and key in dict2:
            dict_diff.append({"name": key, 'value': dict2[key], 'status': 'added'})
        if key in dict1 and key not in dict2:
            dict_diff.append({"name": key, 'value': dict1[key], 'status': 'removed'})
        if key in dict1 and key in dict2 and dict1[key] != dict2[key] and \
                isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            dict_diff.append({"name": key, 'children': compare_dicts(dict1[key], dict2[key]),
                              'status': 'updated_dict'})
        if key in dict1 and key in dict2 and dict1[key] != dict2[key] and not \
                (isinstance(dict1[key], dict) and isinstance(dict2[key], dict)):
            dict_diff.append({"name": key, 'old_value': dict1[key], 'new_value': dict2[key], 'status': 'updated'})
    return dict_diff


def get_name(node):
    return node["name"]

    def get_children(node):
        return node.get("children")


def is_inner(node):
    return "children" in node


def is_leaf(node):
    return not "children" in node


def print_children(tree): # доработать
    def walk(nod, path):
        for child in nod:
            # if path!="":
            print(path)
            child.update({"path": path})
            path = f"{path}.{get_name(child)}"
            # if is_leaf(child):
            #    path=""
            print(child)
            print("children" in child)
            print(path)
            if isinstance(get_children(child), list):
                walk(get_children(child), path)

    return walk(tree, "")