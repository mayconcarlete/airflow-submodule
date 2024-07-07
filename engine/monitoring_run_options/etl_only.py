import sys
from engine.dynamic_import.main import load_function_to_memory
from engine.utils.utils import parse_config_to_dict

def run_etl(monitoring_base_path: str) -> None:
    monitoring_etl_path = f'{monitoring_base_path}/etl/entrypoint.py'
    entrypoint = load_function_to_memory(monitoring_etl_path, "entrypoint")

    monitoring_config_path = f'{monitoring_base_path}/config.json'
    config = parse_config_to_dict(monitoring_config_path)
    print("run_etl")
    data = entrypoint(**config)
   