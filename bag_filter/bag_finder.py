from pathlib import Path
from typing import List


def find_bags(path: str) -> List[str]:
    p = Path(path)

    if not p.exists():
        print(f"Giving path: {path} does not exist.")
        return []

    try:
        return [str(bag_file.resolve()) for bag_file in p.rglob("*.bag")]

    except OSError as e:
        print(f"Error finding bags: {e}")
        return []
