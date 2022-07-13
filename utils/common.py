import yaml


def read_config(config_file):
    with open(config_file, "r") as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content


