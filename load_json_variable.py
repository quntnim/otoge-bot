from typing import Any
import json

def get_parameter(key: str) -> Any:
    with open('./parameter.json') as f:
        return json.load(f)[key]
