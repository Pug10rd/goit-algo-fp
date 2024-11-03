import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, depth):
    if depth == 0:
        return

    x2 = x + length * np.cos(angle)
    y2 = y + length * np.sin(angle)

    plt.plot([x, x2], [y, y2], color='green')
    draw_tree(x2, y2, angle - np.pi / 4, length * 0.7, depth - 1)
    draw_tree(x2, y2, angle + np.pi / 4, length * 0.7, depth - 1)

plt.figure()
draw_tree(0, 0, np.pi / 2, 100, 10)
plt.show()
