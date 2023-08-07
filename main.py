from simple_term_menu import TerminalMenu
from engine.monitoring_factory.monitoring_factory import create_monitoring
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
    menu = Menu()
    menu.print_menu()