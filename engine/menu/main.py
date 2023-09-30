import os
import sys
from simple_term_menu import TerminalMenu
from engine.monitoring_factory.monitoring_factory import create_monitoring

class Menu:
  def run(self) -> None:
    options = ["Create Monitoring", "Run Existing Monitoring"]
    first_level_menu = TerminalMenu(options)

    first_level_option = first_level_menu.show()
    # 0 = create monitoring - 1 Run Existing monitoring
    if first_level_option == 0:
      create_monitoring()

    elif first_level_option == 1:
      monitoring_path = f'{sys.path[0]}/monitorings'
      monitoring_options = os.listdir(monitoring_path)

      items_to_exclude = ["__pycache__", ".gitkeep"]
      for item in items_to_exclude:
        monitoring_options.remove(item)

      monitoring_menu = TerminalMenu(monitoring_options)
      monitoring_index = monitoring_menu.show()

      monitoring_name = monitoring_options[monitoring_index]
      monitoring_base_path = f'{sys.path[0]}/monitorings/{monitoring_name}'
      monitoring_config_path = f'{monitoring_base_path}/config.json'
      monitoring_etl_path = f'{monitoring_base_path}/etl/entrypoint.py'
      monitoring_model_path = f'{monitoring_base_path}/model/model.py'

      monitoring_run_options = ["Run only the ETL.","Run a model with an existing ETL.","Run End to End(this option will create an etl)."]
      run_options_choosed = TerminalMenu(monitoring_run_options).show()
      #  0 = will navigate through the existing ETL flow.
      if run_options_choosed == 0:
        pass
      # 1 Will navigate through the e2e flow.


    return