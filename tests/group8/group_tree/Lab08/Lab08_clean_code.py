import time

# List of names
names = ["john doe", "jane smith", "bob johnson"]
valid_name_count = 0

for name in names:
    # Split the name into first and last name
    split_name = name.split()
    if len(split_name) == 2:  # Check if the name has exactly two parts
        print(f"{split_name[0]} {split_name[1]}")
        valid_name_count += 1
    time.sleep(1)  # Simulate delay

print(f"Total valid names: {valid_name_count}")