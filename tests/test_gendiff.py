from gendiff.functions.functions import generate_diff
file = open('./tests/fixtures/expected.txt', 'r')
result = file.read()
file_nested = open('./tests/fixtures/expected_nested.txt', 'r')
result_nested = file_nested.read()

def test_flat_files():
    assert result == generate_diff('./tests/fixtures/test_before.json', './tests/fixtures/test_after.json')
    assert result == generate_diff('./tests/fixtures/test_before.yml', './tests/fixtures/test_after.yml')


def test_nested_files():
    assert result_nested == generate_diff('./tests/fixtures/test_before_nested.json', './tests/fixtures/test_after_nested.json')
    assert result_nested == generate_diff('./tests/fixtures/test_before_nested.yaml', './tests/fixtures/test_after_nested.yml')
