import json


TAB = 2


def json_from_dict(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))


def encode(file, x):
    return json.dumps(file, indent=x)


def sort(sortable_list):
    return sorted(sortable_list, key=lambda items: items[0][2])


def ready_list(file_1, file_2):
    dict1 = json_from_dict(file_1)
    dict2 = json_from_dict(file_2)
    res = {}

    for key in dict1.keys():
        if dict2.get(key):
            if dict1[key] == dict2[key]:
                res[f"{key}"] = dict1.get(key)
            else:
                res[f"+ {key}"] = dict1.get(key)
                res[f"- {key}"] = dict2.get(key)
        else:
            res[f'- {key}'] = dict1.get(key)
    for key in dict2.keys():
        if dict1.get(key) is None:
            res[f'- {key}'] = dict2.get(key)

    return res


def generate_diff(file_1, file_2):
    return encode(ready_list(file_1, file_2), TAB,
                  ).replace('"', '').replace(',', '')
