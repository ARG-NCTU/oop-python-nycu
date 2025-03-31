def greedy_algorithm(items, capacity):
    """
    A greedy algorithm to solve the fractional knapsack problem.
    :param items: List of tuples where each tuple contains (value, weight)
    :param capacity: Maximum weight capacity of the knapsack
    :return: Maximum value that can be obtained
    """
    # Sort items by value-to-weight ratio in descending order
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    for value, weight in items:
        if capacity >= weight:
            # Take the whole item
            total_value += value
            capacity -= weight
        else:
            # Take the fraction of the item that fits
            total_value += value * (capacity / weight)
            break

    return total_value


# Example usage
if __name__ == "__main__":
    items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
    capacity = 50
    max_value = greedy_algorithm(items, capacity)
    print(f"Maximum value: {max_value}")