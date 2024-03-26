from gendiff.formatters.form_selector import select_formatter
from gendiff.comparison_tree import compare_dicts
from gendiff.parsing_functions import (get_data_and_extension,
                                       parse)


def generate_diff(path_to_file1, path_to_file2, format_name="stylish"):
    dict1 = parse(*get_data_and_extension(path_to_file1))
    dict2 = parse(*get_data_and_extension(path_to_file2))
    dict_diff = compare_dicts(dict1, dict2)
    return select_formatter(dict_diff, format_name)
