import json


def stylish(dict_diff: dict):
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
