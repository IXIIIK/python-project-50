import pytest
import json
import yaml
from gendiff import generate_diff

JSON1 = 'tests/fixture/file1.json'
JSON2 = 'tests/fixture/file2.json'
YAML1 = 'tests/fixture/file1.yml'
YAML2 = 'tests/fixture/file2.yml'


def open_correct_view():
    with open('./tests/fixture/right_stylish_format.txt') as stylish:
        right_stylish = stylish.read()
    with open('./tests/fixture/right_plain_format.txt') as plain:
        right_plain = plain.read()
    return right_stylish, right_plain


def test_generate_diff_json():
    res = open_correct_view()[0].replace('\n', '')
    gen_diff = generate_diff(JSON1, JSON2).replace('\n', '')
    assert res == gen_diff


#def test_generate_diff_yaml():
#   assert open_correct_view()[1] == generate_diff(JSON1, JSON2)


