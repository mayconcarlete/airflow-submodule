import sys
import datetime
import csv

from engine.dynamic_import.main import load_function_to_memory
from engine.utils.utils import parse_config_to_dict

def run_etl(monitoring_name: str) -> None:
    monitoring_base_path = f'{sys.path[0]}/monitorings/{monitoring_name}'
    monitoring_etl_path = f'{monitoring_base_path}/etl/entrypoint.py'

    etl_function = load_function_to_memory(monitoring_etl_path, "entrypoint")

    monitoring_config_path = f'{monitoring_base_path}/config.json'
    config = parse_config_to_dict(monitoring_config_path)

    # dict[str, pd.DataFrame]
    data = etl_function(config)
    data_to_dict = dict
    for key, value in data.items():
        data_to_dict[key]: value.to_dict()

    # save to CSV MONITORING_NAME_DATE
    date = datetime.datetime.now()
    create_date = f'{date.year}-{date.month}-{date.day}-{date.hour}:{date.minute}:{date.second}'
    csv_filename = f'{monitoring_name}_{create_date}'
    with open(f'{csv_filename}.csv', 'w') as f:
