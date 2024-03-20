def compare_dicts(dict1, dict2):
    keys = list(set(dict1.keys()) | set(dict2.keys()))
    keys.sort()
    dict_diff = []
    for key in keys:
        old_value = dict1.get(key)
        new_value = dict2.get(key)
        if key in dict1 and key not in dict2:  # key only in first dict
            dict_diff.append({"name": key,
                              'value': old_value, 'status': 'removed'})
        elif key not in dict1 and key in dict2:  # key only in second dict
            dict_diff.append({"name": key,
                              'value': new_value, 'status': 'added'})
        elif isinstance(old_value, dict) and isinstance(new_value,
                                                        dict):  # for nested
            dict_diff.append({"name": key,
                              'children': compare_dicts(old_value, new_value),
                              'status': 'nested'})
        elif old_value != new_value:
            dict_diff.append({"name": key, 'old_value': old_value,
                              'new_value': new_value, 'status': 'updated'})
        elif old_value == new_value:
            dict_diff.append({"name": key, 'value': old_value,
                              'status': 'same'})
        if isinstance(old_value, dict) and not \
                isinstance(new_value, dict):  # for first nested
            dict_diff[-1].update({'children': compare_dicts(old_value,
                                                            old_value)})
        if not isinstance(old_value, dict) and\
                isinstance(new_value, dict):  # for second nested
            dict_diff[-1].update({'children': compare_dicts(new_value,
                                                            new_value)})
    return dict_diff
