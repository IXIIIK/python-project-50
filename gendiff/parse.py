import json
import yaml
from pathlib import Path


def parse(file_path, data_type):

    with Path(file_path).open() as file:
        if data_type == 'JSON':
            return json.load(file)
        elif data_type == 'YAML':
            return yaml.safe_load(file)
        else:
            raise Exception('Unsupported file format!')


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
