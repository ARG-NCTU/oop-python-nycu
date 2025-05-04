import matplotlib.pyplot as plt

N = [(0, 0), (0, 10), (5, 0), (5, 10)]
Y = [(10, 10), (12.5, 5), (15, 10), (12.5, 5), (12.5, 0)]
C = [(20, 0), (18, 0), (17, 2), (17, 8), (18, 10), (20, 10)]
U = [(25, 10), (25, 2), (27, 0), (29, 2), (29, 10)]

def draw_letter_path(coords, color, label):
    x = [pt[0] for pt in coords]
    y = [pt[1] for pt in coords]
    plt.plot(x, y, marker='o', color=color, label=label)

plt.figure(figsize=(10, 5))
draw_letter_path(N, "red", "N")
draw_letter_path(Y, "green", "Y")
draw_letter_path(C, "blue", "C")
draw_letter_path(U, "purple", "U")

plt.title("NYCU Path")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()

