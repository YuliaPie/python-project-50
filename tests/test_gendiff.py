from gendiff.scripts.gendiff import generate_diff

file_stylish = open('./tests/fixtures/expected_stylish.txt', 'r')
result_stylish = file_stylish.read()
file_plain = open('./tests/fixtures/expected_plain.txt', 'r')
result_plain = file_plain.read()
file_json = open('./tests/fixtures/expected_json.txt', 'r')
result_json = file_json.read()
file_nested_stylish = open('./tests/fixtures/expected_nested_stylish.txt', 'r')
result_nested_stylish = file_nested_stylish.read()
file_nested_plain = open('./tests/fixtures/expected_nested_plain.txt', 'r')
result_nested_plain = file_nested_plain.read()
file_nested_json = open('./tests/fixtures/expected_nested_json.txt', 'r')
result_nested_json = file_nested_json.read()


def test_flat_files_stylish():
    assert result_stylish == \
           generate_diff('./tests/fixtures/'
                         'test_before.json',
                         './tests/fixtures/'
                         'test_after.json')
    assert result_stylish == \
           generate_diff('./tests/fixtures/'
                         'test_before.yml',
                         './tests/fixtures/'
                         'test_after.yml')


def test_flat_files_plain():
    assert result_plain == \
           generate_diff('./tests/'
                         'fixtures/test_before.json',
                         './tests/'
                         'fixtures/test_after.json',
                         "plain")
    assert result_plain == \
           generate_diff('./tests/'
                         'fixtures/test_before.yml',
                         './tests/'
                         'fixtures/test_after.yml',
                         "plain")


def test_nested_files_stylish():
    assert result_nested_stylish == \
           generate_diff('./tests/'
                         'fixtures/test_before_nested.json',
                         './tests/'
                         'fixtures/test_after_nested.json',
                         "stylish")
    assert result_nested_stylish == \
           generate_diff('./tests/'
                         'fixtures/test_before_nested.yaml',
                         './tests/'
                         'fixtures/test_after_nested.yml',
                         "stylish")


def test_nested_files_plain():
    assert result_nested_plain == \
           generate_diff('./tests/'
                         'fixtures/test_before_nested.json',
                         './tests/'
                         'fixtures/test_after_nested.json',
                         "plain")
    assert result_nested_plain == \
           generate_diff('./tests/'
                         'fixtures/test_before_nested.yaml',
                         './tests/'
                         'fixtures/test_after_nested.yml',
                         "plain")


def test_flat_files_json():
    assert result_json == \
           generate_diff('./tests/fixtures/'
                         'test_before.json',
                         './tests/fixtures/'
                         'test_after.json', "json")
    assert result_json == \
           generate_diff('./tests/fixtures/'
                         'test_before.yml',
                         './tests/fixtures/'
                         'test_after.yml',
                         "json")


def test_nested_files_json():
    assert result_nested_json == \
           generate_diff('./tests/fixtures/'
                         'test_before_nested.json',
                         './tests/fixtures/'
                         'test_after_nested.json',
                         "json")
    assert result_nested_json == \
           generate_diff('./tests/fixtures/'
                         'test_before_nested.yaml',
                         './tests/fixtures/'
                         'test_after_nested.yml', "json")
