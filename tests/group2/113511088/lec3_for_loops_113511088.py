####################
# EXAMPLE: while loops and strings
# CHALLENGE: rewrite while loop with a for loop
####################

AN_LETTERS = "aefhilmnorsxAEFHILMNORSX"


def cheer_word(word: str, times: int) -> None:
    """
    模仿原本的程式：
      1. 逐字母喊口號，遇到 an_letters 裡的字母用 'an'，其餘用 'a'
      2. 印出 'What does that spell?'
      3. 印出 times 次的「word !!!」
    這裡用 for 迴圈來實作（不用 while）
    """
    # 用 for 迴圈取代原本的 while 迴圈
    for char in word:
        if char in AN_LETTERS:
            print("Give me an " + char + "! " + char)
        else:
            print("Give me a  " + char + "! " + char)

    print("What does that spell?")
    for _ in range(times):
        print(word, "!!!")
