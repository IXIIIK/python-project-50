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
