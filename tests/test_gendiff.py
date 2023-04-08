import pytest
import json
from gendiff import gendiff

JSON1 = 'tests/fixture/file1.json'
JSON2 = 'tests/fixture/file2.json'
YAML1 = 'tests/fixture/file1.yml'
YAML2 = 'tests/fixture/file2.yml'


@pytest.fixture
def json1():
    return json.load(open(JSON1))


@pytest.fixture
def json2():
    return json.load(open(JSON2))



def test_json1_to_dict():
    result = gendiff.json_yaml_from_dict(JSON1)
    assert result == ({
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
        })

    result = gendiff.json_yaml_from_dict(JSON2)
    assert result == ({
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
        })
    
    result = gendiff.json_yaml_from_dict(YAML1)
    assert result == ({
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
        })

    result = gendiff.json_yaml_from_dict(YAML2)
    assert result == ({
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
        })
    

def test_encode(json2):
    result = gendiff.encode(json2, 0)
    result = result.replace('\n', '')
    assert result == '{"timeout": 20,"verbose": true,"host": "hexlet.io"}'
   

def test_ready_list():
    result = gendiff.ready_list(JSON1, JSON2)
    assert result == {
        '  host': 'hexlet.io',
        '+ timeout': 20,
        '- timeout': 50,
        '- proxy': '123.234.53.22',
        '- follow': False,
        '+ verbose': True
        }

    

