import sys
from engine.menu.main import Menu
from engine.monitoring_factory.monitoring_factory import create_monitoring
from engine.dynamic_import.main import load_function_to_memory
from engine.utils.utils import parse_config_to_dict
import pandas as pd
from simple_term_menu import TerminalMenu

if __name__ == "__main__":
    menu = Menu()
    result = menu.run()

    data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, None]
    }

    data2 = {
        "calories3": [2420, 2380, 2390],
        "duration3": [250, 240, 245]
    }

    dataframe = pd.DataFrame(data)
    dataframe2 = pd.DataFrame(data2)

    dicta = dataframe.to_dict()
    results = {
        "users": dataframe,
        "ufh": dataframe2
    }

    data_to_dict = {}

    for key, values in results.items():
        # data_to_dict[key] = values.to_dict()
        values.to_csv(f'{key}.csv')

    # for key, value in data_to_dict.items():
        # print(key, value)

    # df_all = pd.DataFrame(data_to_dict)
    # df_all.to_csv("data.csv")

    # load_df = pd.read_csv("data.csv", index_col=0)

    # new_dict = load_df.to_dict()
    # parseado = {}
    # for key, values in new_dict.items():
    #     parseado[key] = pd.DataFrame(values, index=[0])

    # print(parseado["users"])
