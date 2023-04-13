from itertools import chain


def normalize_value(data):
    if data is None:
        return 'null'
    if data not in (False, True):
        return data
    else:
        return str(data).lower()


def stylish(data, replacer=' ', level=0, spaces_count=4):
    if not isinstance(data, list):
        return data
    level_indent = replacer * level * spaces_count
    level += 1
    a = list(map(
        lambda data: f"{level_indent} {data[0] if data[0] else replacer} {data[1]}: {normalize_value(stylish(data[2], level=level))}", data))  # noqa: E501
    b = list(chain('{', a, [level_indent + '}']))
    return '\n'.join(b)
