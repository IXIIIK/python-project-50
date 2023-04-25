import pytest
from pathlib import Path
from gendiff import generate_diff
from gendiff.parser import parseargs


def get_data_from_file(file_name):
    with Path(get_full_file_name(file_name)).open() as file:
        result = file.read()
    return result


def get_full_file_name(file_name):
    return f'tests/fixture/{file_name}'


def get_data(file_name):
    if isinstance(file_name, tuple):
        start_data = get_data_from_file(file_name[0])
        end_data = get_data_from_file(file_name[1])
        result = ' '.join((start_data, end_data))
    else:
        result = get_data_from_file(file_name)
    return result


def test_unsupported_files():
    with pytest.raises(Exception) as e:
        _ = generate_diff('some_file1.txt', 'some_file2.txt')
    assert str(e.value) == "Unsupported file format!"


def test_parser():
    parser = parseargs(['file1.json', 'file2.json'])
    assert parser.first_file == 'file1.json'
    assert parser.second_file == 'file2.json'