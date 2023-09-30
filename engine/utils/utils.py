import json

def parse_config_to_dict(path:str) -> dict:
    with open(path, "r") as config_file:
        json_as_string = config_file.read()
        return json.loads(json_as_string)

def save_etl_to_csv(filename: str) -> None:
    pass