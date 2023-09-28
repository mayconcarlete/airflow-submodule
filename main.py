import sys
import types
from importlib.util import spec_from_file_location, module_from_spec
from simple_term_menu import TerminalMenu
from engine.monitoring_factory.monitoring_factory import create_monitoring
from engine.common.utils import load_config_file_to_dict
from monitorings import available_monitorings
import monitorings.teste.etl.entrypoint
class Menu:
    def __init__(self) -> None:
        self.options = ["Create Monitoring", "Run Moniroting"]
        self.options_two = ["locally", "live"]

    def print_menu(self) -> int:
        terminal_menu = TerminalMenu(self.options)

        terminal_sub_menu = TerminalMenu(self.options_two)
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            create_monitoring()
        return menu_entry_index


if __name__ == "__main__":
    # menu = Menu()
    # menu.print_menu()
    monitoring_name = "teste"
    path = f'{sys.path[0]}/monitorings/{monitoring_name}/config.json'
    path_to_etl = f'{sys.path[0]}/monitorings/{monitoring_name}/etl/entrypoint.py'
    config = load_config_file_to_dict(path)

    spec = spec_from_file_location("entrypoint", path_to_etl)
    modulo = module_from_spec(spec)
    sys.modules[modulo] = modulo
    spec.loader.exec_module(modulo)

    funcao = getattr(modulo, "entrypoint")
    funcao(**config)

    # funcao.entrypoint(**config)
    # available_monitorings[monitoring_name].entrypoint(**config)

    # monitorings[monitoring_name].entrypoint(**config)