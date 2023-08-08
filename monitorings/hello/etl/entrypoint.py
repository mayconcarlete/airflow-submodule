import pandas as pd

def entrypoint(** kwargs)-> dict[str, pd.DataFrame]:
    print("Available resources")
    print(kwargs)
    data = {
      "calories": [420, 380, 390],
      "duration": [50, 40, 45]
    }
    return {
        "training": pd.DataFrame(data)
    }
