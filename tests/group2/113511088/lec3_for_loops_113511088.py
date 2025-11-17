####################
# EXAMPLE: for loops over strings
####################

def print_i_or_u_by_index(s: str) -> None:
    """用 index 走訪字串，遇到 i 或 u 就印一句話"""
    for index in range(len(s)):
        if s[index] == 'i' or s[index] == 'u':
            print("There is an i or u")


def print_i_or_u_by_char(s: str) -> None:
    """直接用字元走訪字串，遇到 i 或 u 就印一句話"""
    for char in s:
        if char == 'i' or char == 'u':
            print("There is an i or u")
