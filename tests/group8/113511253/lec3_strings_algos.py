def is_palindrome(s):
    clean_s = ''.join(c.lower() for c in s if c.isalpha())
    return clean_s == clean_s[::-1]

def cheer_word(word, n):
    lines = []
    for char in word:
        lines.append(f"Give me an {char}! {char}")
    lines.append("What does that spell?")
    final = f"{word} !!!"
    for _ in range(n):
        lines.append(final)
    return lines
