import numpy as np
from scipy.special import jv, yv, iv
import matplotlib.pyplot as plt
import matplotlib as mpl

print(mpl.rcParams.keys())
mpl.rcParams.update({"font.size": 26, "text.usetex":True, "text.latex.preamble":r"\usepackage{amsmath}"})

fig, ax = plt.subplots(figsize=(12, 8))
fs = lambda n: rf"$\mathit{{J}}_{n}$"

areas = (
    np.array(
        [0.005113688, 0.016728375, 0.035550522, 0.105989022, 0.214107707, 0.359649334]
    )
    * 0.08
)
relstd = np.array(
    [
        3.35e-03,
        6.39e-04,
        1.45e-04,
        1.20e-04,
        1.08e-04,
        9.82e-05,
    ]
)

ax.semilogy(areas, relstd, linewidth=3)
# ax.legend(fontsize=15)
ax.set_xlabel(r"$\text{Coil area}\cdot\text{Peak Field Strength}$")
# ax.set_xlim([0, 10])
ax.text(1.05, 0, r"Wb", transform=ax.transAxes)

ax.set_ylabel("Normalized Std. Deviation")
# ax.set_ylim([-1,0.6])
# ax.set_yticks([-0.4, 0, 0.4, 0.8, 1])
# ax.get_yaxis().set_label_coords(0, 1.05, transform=ax.transAxes)

# ax.axhline(color="grey")

ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
plt.savefig("calcs/areatofield.png")
