import numpy as np
from scipy.special import jv, yv, iv
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({"font.size": 26})

fig, ax = plt.subplots(figsize=(12, 8))
x = np.linspace(0, 10, 1000)
fntSize = 26
f = jv
fs = lambda n: rf"$\mathit{{J}}_{n}$"

for n in range(5):
    l = ax.plot(x, f(n, x), label=rf"{fs(n)}", linewidth=2)
    ax.text(
        np.max([x[np.argmax(f(n, x))] * 1.01, 0.15]),
        1.05 * np.max(f(n, x)),
        l[-1].get_label(),
        fontsize=fntSize - 2,
        color=l[-1].get_color(),
    )

# ax.legend(fontsize=15)
ax.set_xlabel(r"$x$", fontsize=fntSize)
ax.set_xlim([0, 10])
ax.get_xaxis().set_label_coords(1.05, 0, transform=ax.transAxes)

ax.set_ylabel(fr"{fs('n')}$(x)$", fontsize=fntSize, rotation=0)
#ax.set_ylim([-1,0.6])
ax.set_yticks([-0.4, 0, 0.4, 0.8, 1])
ax.get_yaxis().set_label_coords(0, 1.05, transform=ax.transAxes)

ax.axhline(color="grey")

ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
plt.savefig("calcs/Jnplot.pdf")
