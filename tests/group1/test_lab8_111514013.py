def test_lab8_111514013():
    """
    This function is a placeholder for the test case.
    It does not perform any operations.
    """
    pass
    # Import time library
    import time

    # Create a list of names
    name_list = ["john doe", "jane smith", "bob johnson"]

    # Initialize a counter for the total number of names
    total_names_count = 0

    for name in name_list:
        # Split the name into first and last name
        first_last_name_list = name.split()

        # Check if the first_last_name_list has exactly two parts (first and last name)
        if len(first_last_name_list) == 2:
            # Print the full name
            # [0]: first name, [1]: last name
            print(first_last_name_list[0] + " " + first_last_name_list[1])

            # Increment the counter
            total_names_count += 1

        # Pause for 1 second before processing the next name
        time.sleep(1)

    # Print the total number of names processed
    print("total: " + str(total_names_count))

# This is a test function for lab8_111514013
test_lab8_111514013()