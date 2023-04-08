import json
import yaml


INDEX = 2


def json_yaml_from_dict(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return yaml.load(open(file_path), Loader=yaml.FullLoader)


def encode(file, index):
    return json.dumps(file, indent=index)





def ready_list(file_1, file_2):
    dict1 = json_yaml_from_dict(file_1)
    dict2 = json_yaml_from_dict(file_2)
    res = {}

    for key in dict1.keys():
        if dict2.get(key):
            if dict1[key] == dict2[key]:
                res[f"  {key}"] = dict1.get(key)
            else:
                res[f"- {key}"] = dict1.get(key)
                res[f"+ {key}"] = dict2.get(key)
        else:
            res[f'- {key}'] = dict1.get(key)
    for key in dict2.keys():
        if dict1.get(key) is None:
            res[f'+ {key}'] = dict2.get(key)

    return res


def generate_diff(file_1, file_2):
    return encode(ready_list(file_1, file_2),
                INDEX).replace('"', '').replace(',', '')


