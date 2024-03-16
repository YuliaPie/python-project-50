def compare_dicts(dict1, dict2):
    keys = list(set(dict1.keys()) | set(dict2.keys()))
    keys.sort()
    dict_diff = []
    for key in keys:
        if key in dict1 and key in dict2 and dict1[key] == dict2[key]:
            dict_diff.append({"name": key,
                              'value': dict1[key], 'status': 'same'})
        if key not in dict1 and key in dict2:
            dict_diff.append({"name": key,
                              'value': dict2[key], 'status': 'added'})
        if key in dict1 and key not in dict2:
            dict_diff.append({"name": key,
                              'value': dict1[key], 'status': 'removed'})
        if key in dict1 and key in dict2 and dict1[key] != dict2[key] and \
                isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            dict_diff.append({"name": key,
                              'children': compare_dicts(dict1[key], dict2[key]),
                              'status': 'updated_dict'})
        if key in dict1 and key in dict2 and dict1[key] != dict2[key] and not \
                (isinstance(dict1[key], dict) and isinstance(dict2[key], dict)):
            dict_diff.append({"name": key, 'old_value': dict1[key],
                              'new_value': dict2[key], 'status': 'updated'})
    return dict_diff
