import time
from typing import List

def process_names(names: List[str]) -> int:

    valid_name_count = 0

    for full_name in names:
        name_parts = full_name.split()

        if len(name_parts) == 2:
            first_name, last_name = name_parts
            print(f"{first_name} {last_name}")
            valid_name_count += 1

        time.sleep(1)

    return valid_name_count


if __name__ == "__main__":

    full_name_list = ["john doe", "jane smith", "bob johnson"]

    total_valid = process_names(full_name_list)

    print(f"Total valid names: {total_valid}")

