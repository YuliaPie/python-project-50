import pytest
import json
from gendiff.scripts.gendiff import generate_diff

file = open('./tests/fixtures/expected.txt', 'r')
result = file.read()


def test_flat_files():
    assert result == generate_diff('./tests/fixtures/test_before.json', './tests/fixtures/test_after.json')
