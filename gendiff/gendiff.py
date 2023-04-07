import json


def json_from_dict(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))


def encode(file):
    return json.dumps(dict(file), indent=2)


def sort(sortable_list):
    return sorted(sortable_list, key=lambda items: items[0][2])


def ready_list(file_1, file_2):
    dict1 = json_from_dict(file_1)
    dict2 = json_from_dict(file_2)
    res = []

    for key in dict1.keys():
        if dict2.get(key):
            if dict1[key] == dict2[key]:
                res.append((f'{key}', dict1.get(key)))
            else:
                res.append((f'+ {key}', dict1.get(key)))
                res.append((f'- {key}', dict2.get(key)))
        else:
            res.append((f'{key}', dict1.get(key)))
    for key in dict2.keys():
        if dict1.get(key) is None:
            res.append((f'+ {key}', dict1.get(key)))

    return res


def generate_diff(file_1, file_2):
    return encode(sort(ready_list(file_1, file_2),
                       )).replace('"', '').replace(',', '')
