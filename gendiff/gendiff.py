import json
import yaml
from gendiff.formaters.plain import flatten
from gendiff.formaters.stylish import stylish

GET_FORMAT = {
    'stylish': stylish,
    'plain': flatten,
    #'json': get_json
}

INDEX = 2


def json_yaml_from_dict(file_path):
        if file_path.endswith('.yaml') or file_path.endswith('.yml'):  # noqa: E117, E501
            with open(file_path) as f:
                file_yaml = yaml.safe_load(f)
                return file_yaml
        elif file_path.endswith('.json'):
            with open(file_path) as f:
                file_json = json.load(f)
                return file_json
        else:
            raise Exception("Invalid file format")


def ready_list(file_1, file_2, level=1):  # noqa: C901
    keys = file_1.keys() | file_2.keys()
    res = []

    for key in sorted(keys):
        if key not in file_2:
            res.append(('-', key, get_children(file_1.get(key))))
        elif key in file_1 and file_2:
            if not (isinstance(file_1[key], dict) and isinstance(file_2[key], dict)):  # noqa: E501
                if file_1[key] == file_2[key]:
                     res.append((' ', key, get_children(file_1.get(key))))  # noqa: E111, E117, E501
                elif file_1[key] != file_2[key]:
                    res.append(('-', key, get_children(file_1.get(key))))
                    res.append(('+', key, get_children(file_2.get(key))))
            else:
                res.append((' ', key, ready_list(file_1[key], file_2[key])))
        else:
            res.append(('+', key, get_children(file_2.get(key))))

    return res


def get_children(data):
    if not isinstance(data, dict):
        return data
    res = []
    for key, value in data.items():
        res.append((' ', key, get_children(value)))
    return res


def generate_diff(file_1, file_2, format='stylish'):
    file_1 = json_yaml_from_dict(file_1)
    file_2 = json_yaml_from_dict(file_2)
    diff = ready_list(file_1, file_2)
    return GET_FORMAT[format](diff)
