from typing import List, Optional
from .bag_finder import find_bags
from .bag_filter import filter_bags
from .config_parser import load_config

import pkg_resources


def get_default_config() -> str:
    return pkg_resources.resource_filename("bag_filter", "config/config.yaml")


def filter_bags_by_config(
    bag_path: str, config_path: Optional[str] = None
) -> List[str]:
    if config_path is None:
        config_path = get_default_config()

    bags_list = find_bags(bag_path)
    config = load_config(config_path)
    filtered_bags = filter_bags(bags_list, config)
    return filtered_bags


__all__ = ["filter_bags_by_config", "get_default_config"]

__version__ = "0.1.0"
