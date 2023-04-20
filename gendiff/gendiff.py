from gendiff.parse import parse
from gendiff.parse import get_data_type
from gendiff.formaters.plain import flatten
from gendiff.formaters.stylish import stylish
from gendiff.formaters.json import get_json


def formatting(result_dict, format_name):
    if format_name == "stylish":
        return stylish(result_dict)
    elif format_name == "plain":
        return flatten(result_dict)
    elif format_name == "json":
        return get_json(result_dict)
    else:
        return "Неизвестный формат для вывода результата сравнения"


def make_tree(data1, data2):
    return {"type": "root", "children": make_children(data1, data2)}


def make_children(data1, data2):  # noqa: C901
    result = []
    keys = data1.keys() | data2.keys()
    for key in sorted(keys):
        if key not in data2:
            result.append({"key": key, "type": "deleted", "value": data1[key]})
        elif key not in data1:
            result.append({"key": key, "type": "added", "value": data2[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append(
                {
                    "key": key,
                    "type": "parent",
                    "children": make_children(data1[key], data2[key]),
                }
            )
        elif data1[key] == data2[key]:
            result.append(
                {"key": key, "type": "unchanged", "value": data1[key]}
            )
        else:
            result.append(
                {
                    "key": key,
                    "type": "updated",
                    "value1": data1[key],
                    "value2": data2[key],
                }
            )
    return result


def generate_diff(file_1, file_2, format='stylish'):
    file1 = get_data_type(file_1)
    file2 = get_data_type(file_2)
    return formatting(make_tree(file1, file2), format)
