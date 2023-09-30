from simple_term_menu import TerminalMenu
from engine.monitoring_factory.monitoring_factory import create_monitoring

class Menu:
  def __init__(self) -> None:
    self.options = ["Create Monitoring", "Run Existing Monitoring"]

  def run(self) -> None:
    first_level_menu = TerminalMenu(self.options)
    first_level_option = first_level_menu.show()
    # 0 = create monitoring - 1 Run Existing monitoring
    if first_level_option == 0:
      create_monitoring()