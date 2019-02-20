#!/~/VENV/py3_venv/bin/python3
import yaml
from pprint import pprint as pp


def read_yaml(filename):
    with open(filename) as f:
        for val in (yaml.load_all(f)):
            pp(val)


def write_yaml(filename, output, style=None):
    with open(filename, "wt") as f:
        if style == "compressed":
            yaml.dump(output, f, default_flow_style=True)
        else:
            yaml.dump(output, f, default_flow_style=False) 

