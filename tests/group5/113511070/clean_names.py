import time
from typing import List

def process_names(names: List[str]) -> None:
    valid_name_count = 0

    for full_name in names:
        name_parts = full_name.split()
        if len(name_parts) == 2:
            first_name, last_name = name_parts
            print(f"{first_name} {last_name}")
            valid_name_count += 1
        time.sleep(1)  # 模擬處理延遲

    print(f"Total valid names: {valid_name_count}")

if __name__ == "__main__":
    name_list = ["john doe", "jane smith", "bob johnson"]
    process_names(name_list)

