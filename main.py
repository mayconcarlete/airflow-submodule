import sys
from engine.menu.main import Menu
from engine.monitoring_factory.monitoring_factory import create_monitoring
from engine.dynamic_import.main import load_func_to_memory
from engine.utils.utils import parse_config_to_dict

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
    menu = Menu()
    result = menu.run()
    # menu.print_menu()
    # monitoring_name = "teste"


    # funcao = load_func_to_memory(path_to_etl, "entrypoint")
    # funcao(**config)

    # funcao.entrypoint(**config)
    # available_monitorings[monitoring_name].entrypoint(**config)

    # monitorings[monitoring_name].entrypoint(**config)