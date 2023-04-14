from gendiff.parse_json_yaml import parse
from gendiff.formaters.plain import flatten
from gendiff.formaters.stylish import stylish
from gendiff.formaters.json import get_json


GET_FORMAT = {
    'stylish': stylish,
    'plain': flatten,
    'json': get_json
}


def get_data_type(file_path1, file_path2):

    file1_ext = file_path1[-4:].upper()
    file2_ext = file_path2[-4:].upper()
    yaml_ext = ('.YML', 'YAML')
    if file1_ext == 'JSON' and file2_ext == 'JSON':
        data_type = 'JSON'
    elif file1_ext in yaml_ext and file2_ext in yaml_ext:
        data_type = 'YAML'
    else:
        raise Exception('Unsupported file format!')
    return data_type


def get_diff_for_key(dict1, dict2, key):
    old_data = dict1.get(key, None)
    new_data = dict2.get(key, None)
    if old_data == new_data:
        result = ('unchanged', key, old_data, new_data)
    elif key not in dict1:
        result = ('added', key, old_data, new_data)
    elif key not in dict2:
        result = ('removed', key, old_data, new_data)
    elif isinstance(old_data, dict) and isinstance(new_data, dict):
        result = ('nested', key, ready_list(old_data, new_data), None)
    else:
        result = ('changed', key, old_data, new_data)
    return result


def ready_list(file_1, file_2, level=1):
    result = []
    keys1 = list(file_1.keys())
    keys2 = list(file_2.keys())
    all_keys = sorted(set(keys1 + keys2))
    for key in all_keys:
        result.append(get_diff_for_key(file_1, file_2, key))
    return result


def generate_diff(file_1, file_2, format='stylish'):
    data_type = get_data_type(file_1, file_2)
    parsed_data1 = parse(file_1, data_type)
    parsed_data2 = parse(file_2, data_type)
    diff_list = ready_list(parsed_data1, parsed_data2)
    return GET_FORMAT[format](diff_list)
