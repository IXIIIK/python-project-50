import pytest
from gendiff import generate_diff
from tests.fixture import correct

correct_json = correct.diff_json
correct_yml = correct.diff_yml
correct_stylish_yml = correct.diff_stylish_yml
correct_plain = correct.diff_plain
correct_plain_yaml = correct.diff_plain_yml
correctjson_json = correct.diffjson_json
correctyml_json = correct.diffyml_json

json1 = r'tests/fixture/file1.json'
json2 = r'tests/fixture/file2.json'
yml1 = r'tests/fixture/file1.yml'
yml2 = r'tests/fixture/file2.yml'



@pytest.mark.parametrize("test_input1,test_input2,formatter,expected",
                         [
                             pytest.param(json1, json2, 'stylish', correct_json),
                             pytest.param(yml1, yml2, 'stylish', correct_yml),                                                   
                         ]
                         )
def test_generate_diff(test_input1, test_input2, formatter, expected):
    assert generate_diff(test_input1, test_input2, formatter) == expected


