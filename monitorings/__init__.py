import os
import sys

# import monitorings.teste.etl.entrypoint as teste



print(os.listdir(f'{sys.path[0]}/monitorings'))



available_monitorings = dict()
# available_monitorings["teste"] = teste

__all__ = [available_monitorings]