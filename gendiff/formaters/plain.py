from json import dumps


TYPE = 0
KEY = 1
OLD_VALUE = 2
NEW_VALUE = 3


def flatten(diff, path=''):
    format_vertex_vars = {
        'unchanged': format_unchanged,
        'added': format_added,
        'removed': format_removed,
        'nested': format_nested,
        'changed': format_changed}
    result = []
    for vertex in diff:
        format_vertex = format_vertex_vars[vertex[TYPE]]
        formatted_vertex = format_vertex(vertex, path)
        if formatted_vertex is not None:
            result.append(formatted_vertex)
    result = '\n'.join(result)
    return result


def get_path(path, branch):
    return f'{path}.{branch}' if path else branch


def format_unchanged(vertex, path):
    return None


def format_added(vertex, path):
    return (f"Property '{get_path(path, vertex[KEY])}' "
            f"was added with value: {stringify_value(vertex[NEW_VALUE])}")


def format_removed(vertex, path):
    path = get_path(path, vertex[KEY])
    return f"Property '{path}' was removed"


def format_nested(vertex, path):
    return flatten(vertex[OLD_VALUE], get_path(path, vertex[KEY]))


def format_changed(vertex, path):
    return (f"Property '{get_path(path, vertex[KEY])}' "
            f"was updated. From {stringify_value(vertex[OLD_VALUE])} "
            f"to {stringify_value(vertex[NEW_VALUE])}")


def stringify_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if any((
            isinstance(value, int),
            isinstance(value, bool),
            value is None
    )):
        return value if isinstance(value, str) else dumps(value)
    return f"'{value}'"
