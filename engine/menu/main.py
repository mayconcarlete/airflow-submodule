import os
import sys
from simple_term_menu import TerminalMenu
from engine.monitoring_factory.monitoring_factory import create_monitoring
from engine.monitoring_run_options.etl_only import run_etl

class Menu:
  def run(self) -> None:
    main_menu_options = ["Create Monitoring", "Run Existing Monitoring"]
    main_menu = TerminalMenu(main_menu_options)

    # Display a menu for chooseing between Create or Run an existing monitoring.
    main_menu_option_chosen = main_menu.show()
    # 0 = create monitoring - 1 Run Existing monitoring
    if main_menu_option_chosen == 0:
      create_monitoring()

    elif main_menu_option_chosen == 1:
      # Get the list of available monitorings excluding cache files and .gitkeep.
      monitorings_path = f'{sys.path[0]}/monitorings'
      list_raw_monitoring_folder = os.listdir(monitorings_path)
      files_to_exclude = ["__pycache__", ".gitkeep"]
      list_of_available_monitorings = [monitoring for monitoring in list_raw_monitoring_folder if monitoring not in files_to_exclude]

      # Display a menu for choosing between all available monitorings.
      monitorings_menu = TerminalMenu(list_of_available_monitorings)
      monitoring_option_chosen = monitorings_menu.show()

      monitoring_name = list_of_available_monitorings[monitoring_option_chosen]
      monitoring_base_path = f'{sys.path[0]}/monitorings/{monitoring_name}'
      # monitoring_config_path = f'{monitoring_base_path}/config.json'
      # monitoring_etl_path = f'{monitoring_base_path}/etl/entrypoint.py'
      # monitoring_model_path = f'{monitoring_base_path}/model/model.py'

      # Display a menu for choosing the action for the monitoring.
      monitoring_run_options = ["Run only the ETL.","Run a model with an existing ETL.","Run End to End(this option will create an etl)."]
      run_options_chosen = TerminalMenu(monitoring_run_options).show()
      
      #  0 = It will execute existing ETL flow for the given monitoring saving the data on Minio.
      if run_options_chosen == 0:
        run_etl(monitoring_base_path)
        
      # 1 It will execute the existing Model using an existing data from Minio that got saved by the first or third option.
      if run_options_chosen == 1:
        print(1)

      if run_options_chosen == 2:
        print(2)

    return