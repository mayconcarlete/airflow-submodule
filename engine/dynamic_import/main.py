import sys
from importlib.util import spec_from_file_location, module_from_spec

def load_function_to_memory(file_path: str, name: str) -> object:
  spec = spec_from_file_location(name=name, location=file_path)
  module = module_from_spec(spec=spec)
  sys.modules[module] = module
  spec.loader.exec_module(module)

  return getattr(module, name)