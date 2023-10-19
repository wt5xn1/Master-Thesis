from locale import normalize
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

txtsize = 32
fig = plt.figure()
fig.tight_layout()
ax = plt.axes(projection="3d")

n = 101
t = np.linspace(0, 6 * np.pi, n)
B = np.array([t, np.zeros(n), np.zeros(n)])
ax.plot(B[0], B[1], B[2], color="r", linewidth=4)
ax.quiver(B[0][-1], B[1][-1], B[2][-1], 2, 0, 0, linewidth=4, color="r")
ax.text(B[0][0], B[1][0], B[2][0], r"$\mathbf{B}$", fontsize=txtsize, color="r")

ep = np.array([t, np.cos(t), np.sin(t)])
ax.plot(ep[0], ep[1], ep[2], color="b", linewidth=3)
ax.quiver(
    t[-1], np.cos(t[-1]), np.sin(t[-1]), 1, 0, 1, color="g", normalize=True, length=1
)
ax.quiver(
    t[-1],
    np.cos(t[-1]),
    np.sin(t[-1]),
    0,
    -1,
    0,
    color="orange",
    normalize=True,
    length=0.5,
)
ax.text(t[-1], np.cos(t[-1]), np.sin(t[-1]), "$e^-$", fontsize=txtsize, color="b")
ax.text(
    t[-1],
    np.cos(t[-1]) - 0.55,
    np.sin(t[-1] + 0.1),
    "$F_e$",
    fontsize=txtsize,
    color="orange",
)
ax.text(
    t[-1] + 1,
    np.cos(t[-1]),
    np.sin(t[-1]) + 0.8,
    "$v_e$",
    fontsize=txtsize,
    color="g",
)

ax.grid(False)
ax.axis("off")
plt.show()
