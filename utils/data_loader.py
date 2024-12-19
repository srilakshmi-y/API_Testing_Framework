import json


def load_json_file(file_path):
    """
    Load a JSON file and return its contents as a Python dictionary.
    """
    with open(file_path, "r") as file:
        json_payload = json.load(file)
        return json_payload
