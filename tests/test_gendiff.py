import pytest
import json
from gendiff import gendiff

JSON1 = 'tests/fixture/file1.json'
JSON2 = 'tests/fixture/file2.json'

@pytest.fixture
def json1():
    return json.load(open(JSON1))


@pytest.fixture
def json2():
    return json.load(open(JSON2))



def test_json1_to_dict():
    result = gendiff.json_from_dict(JSON1)
    assert result == ({
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False,
  })

    result = gendiff.json_from_dict(JSON2)
    assert result == ({
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
})
    

    

