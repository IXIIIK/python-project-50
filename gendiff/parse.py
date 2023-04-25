import json
import yaml


def parse(file, format_name):
    if format_name == "JSON":
        return json.load(file)
    elif format_name == "YAML":
        return yaml.safe_load(file)
