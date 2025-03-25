def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return None
    return a / b

if __name__ == '__main__':
    print(subtract(10, 5))
    print(divide(10, 5))
