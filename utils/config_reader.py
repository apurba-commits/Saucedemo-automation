import yaml
import os

def read_config():
    path = os.path.join("config", "config.yaml")
    with open(path, "r") as file:
        return yaml.safe_load(file)
