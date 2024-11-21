import yaml

from typing import Any, Dict
from pathlib import Path


def load_config(config_path: str) -> Dict[str, Any]:
    p = Path(config_path)

    if not p.exists():
        print(f"Config file: {config_path} not found")
        return {"bag_patterns": [], "filters": []}

    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
            if not isinstance(config, dict):
                raise ValueError("Invalid config format")
            config.setdefault("bag_patterns", [])
            config.setdefault("filters", [])
            return config

    except yaml.YAMLError as e:
        print(f"Error parsing config file: {e}")
        return {"bag_patterns": [], "filters": []}

    except Exception as e:
        print(f"Unexpected error reading config: {e}")
        return {"bag_patterns": [], "filters": []}
