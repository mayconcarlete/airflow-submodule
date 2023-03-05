import json

def load_config_file_to_dict(path:str) -> dict:
    with open(path, "r") as config_file:
        json_as_string = config_file.read()
        return json.loads(json_as_string)