import numpy as np
from scipy.special import jv, yv, iv
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({"font.size": 26})

fig, ax = plt.subplots(figsize=(12, 8))
fs = lambda n: rf"$\mathit{{J}}_{n}$"

areas = np.array(
    [0.005113688, 0.016728375, 0.035550522, 0.105989022, 0.214107707, 0.359649334]
)
relstd = np.array([3.35E-03,
6.39E-04,
1.45E-04,
1.20E-04,
1.08E-04,
9.82E-05,
])

ax.semilogy(areas, relstd, linewidth=3)
# ax.legend(fontsize=15)
ax.set_xlabel(r"Coil area")
#ax.set_xlim([0, 10])
ax.text(1.05, 0, "$m^2$", transform=ax.transAxes)

ax.set_ylabel('Normalized Std. Deviation')
# ax.set_ylim([-1,0.6])
#ax.set_yticks([-0.4, 0, 0.4, 0.8, 1])
#ax.get_yaxis().set_label_coords(0, 1.05, transform=ax.transAxes)

#ax.axhline(color="grey")

ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
plt.savefig("calcs/plot.png")
