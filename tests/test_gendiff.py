from gendiff.functions.functions import run
file = open('./tests/fixtures/expected.txt', 'r')
result = file.read()


def test_flat_files():
    assert result == run('./tests/fixtures/test_before.json', './tests/fixtures/test_after.json')
    assert result == run('./tests/fixtures/test_before.yml', './tests/fixtures/test_after.yml')
