from gendiff.parse import parse
from gendiff.formaters.plain import flatten
from gendiff.formaters.stylish import stylish
from gendiff.formaters.json import get_json
from gendiff.compare_data import get_diff_list


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


def generate_diff(file_path1, file_path2, format='stylish'):
    data_type = get_data_type(file_path1, file_path2)
    parsed_data1 = parse(file_path1, data_type)
    parsed_data2 = parse(file_path2, data_type)
    diff_list = get_diff_list(parsed_data1, parsed_data2)
    return GET_FORMAT[format](diff_list)
