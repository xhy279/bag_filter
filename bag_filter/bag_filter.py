from fnmatch import fnmatch
import json
import multiprocessing
import operator
import re
from typing import Any, Dict, List
import rosbag
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

def process_single_bag(bag_path: str, config: Dict[str, Any], lock: Lock, results: List[str]) -> None:
    try:
        with rosbag.Bag(bag_path, 'r') as bag:
            print(f"Processing bag: {bag_path}")
            found_match = False

            # handle each filter
            for filter in config["filters"]:
                if found_match:
                    break

                topic = filter["topic"]
                print(f"Reading messages from topic: {topic}")
                for _, msg, *_ in bag.read_messages(topics=[topic]):
                    if found_match:
                        break

                    entries = getattr(msg, filter["path"])
                    for entry in entries:
                        if found_match:
                            break

                        if re.match(filter["pattern"], entry.data):
                            debug_info_str = re.sub(filter["pattern"], "", entry.data, 1)
                            # only handle json string format debug msg for now
                            debug_info_json = json.loads(debug_info_str)[0]
                            # check if meet any of the conditions and add to filtered_by_filters
                            for condition in filter["conditions"]:
                                if evaluate_condition(debug_info_json, condition):
                                    with lock:
                                        results.append(bag_path)
                                        found_match = True
                                        break
    except Exception as e:
        print(f"Error processing bag {bag_path}: {e}")

def filter_bags(bags_list: List[str], config: Dict[str, Any]) -> List[str]:
    # filter by bag_patterns
    filtered_by_bag_patterns = []
    if "bag_patterns" not in config or not config["bag_patterns"]:
        filtered_by_bag_patterns = bags_list
    else:
        for bag_path in bags_list:
            if any(fnmatch(bag_path, pattern) for pattern in config["bag_patterns"]):
                filtered_by_bag_patterns.append(bag_path)

    worker_count = get_worker_count(len(filtered_by_bag_patterns))

    # filter by filters
    if "filters" not in config or not config["filters"]:
        # if no filters, return filtered_by_bag_patterns
        return filtered_by_bag_patterns
    
    
    filtered_by_filters = []
    lock = Lock()
    # process each bag in parallel
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = [
            executor.submit(process_single_bag, bag_path, config, lock, filtered_by_filters) 
            for bag_path in filtered_by_bag_patterns
        ]
        for future in futures:
            future.result()
    print(filtered_by_filters)
    return filtered_by_filters

def evaluate_condition(data: dict, condition: dict) -> bool:
    operators_map = {
        "==": operator.eq,
        "!=": operator.ne,
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "in": lambda x, y: x in y,
        "not in": lambda x, y: x not in y,
    }
    
    op = operators_map.get(condition["operator"])
    if not op:
        raise ValueError(f"Unsupported operator: {condition['operator']}")
    
    return op(data[condition['field']], condition['value'])

def get_worker_count(bags_len: int) -> int:
    cpu_count = multiprocessing.cpu_count()
    worker_count = cpu_count * 2
    max_workers = min(worker_count, bags_len, 16)
    return max_workers