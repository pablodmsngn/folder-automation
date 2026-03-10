import json


def load_config(config_file: str = 'config.json') -> dict:
    try:
        with open(config_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{config_file}' was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file '{config_file}' has an incorrect format.")
        return {}
