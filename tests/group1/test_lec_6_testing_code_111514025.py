def hanoi(n, source, target, auxiliary):
    moves = []

    def move(fr, to):
        moves.append((fr, to))
        print(f"move from {fr} to {to}")

    def solve(n, fr, to, spare):
        if n == 1:
            move(fr, to)
        else:
            solve(n - 1, fr, spare, to)
            solve(1, fr, to, spare)
            solve(n - 1, spare, to, fr)

    solve(n, source, target, auxiliary)
    print(f"If n = {n}, need to do {len(moves)} moves.\n")
    return moves


# 主程式：執行幾組測試
if __name__ == "__main__":
    hanoi(4, 'P1', 'P2', 'P3')
    hanoi(1, 'P1', 'P2', 'P3')
    hanoi(2, 'P1', 'P2', 'P3')
    hanoi(5, 'P1', 'P2', 'P3')
import pytest
from math import pow

@pytest.mark.parametrize("n, expected_moves", [
    (1, 1),
    (2, 3),
    (3, 7),
    (4, 15),
    (5, 31),
])
def test_hanoi_move_count(n, expected_moves):
    moves = hanoi(n, 'A', 'B', 'C')
    assert len(moves) == expected_moves
