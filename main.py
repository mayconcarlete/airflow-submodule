import sys
from engine.menu.main import Menu
from engine.monitoring_factory.monitoring_factory import create_monitoring
from engine.dynamic_import.main import load_function_to_memory
from engine.utils.utils import parse_config_to_dict
import pandas as pd
# class Menu:
#     def __init__(self) -> None:
#         self.options = ["Create Monitoring", "Run Moniroting"]
#         self.options_two = ["locally", "live"]

#     def print_menu(self) -> int:
#         terminal_menu = TerminalMenu(self.options)

#         terminal_sub_menu = TerminalMenu(self.options_two)
#         menu_entry_index = terminal_menu.show()

#         if menu_entry_index == 0:
#             create_monitoring()
#         return menu_entry_index


if __name__ == "__main__":
    # menu = Menu()
    # result = menu.run()
    # # menu.print_menu()
    # monitoring_name = "teste"


    # funcao = load_func_to_memory(path_to_etl, "entrypoint")
    # funcao(**config)

    # funcao.entrypoint(**config)
    # available_monitorings[monitoring_name].entrypoint(**config)

    # monitorings[monitoring_name].entrypoint(**config)


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
        data_to_dict[key] = values.to_dict()


    # for key, value in data_to_dict.items():
        # print(key, value)

    df_all = pd.DataFrame(data_to_dict)
    df_all.to_csv("data.csv")

    load_df = pd.read_csv("data.csv", index_col=0)

    new_dict = load_df.to_dict()
    parseado = {}
    for key, values in new_dict.items():
        parseado[key] = pd.DataFrame(values, index=[0])

    print(parseado["users"])