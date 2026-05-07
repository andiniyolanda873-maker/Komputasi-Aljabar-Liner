# =========================================================
# VISUALISASI TRANSFORMASI CERMIN
# OTOMATIS MEMBUAT cermin.gif
# =========================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# =========================================================
# TITIK
# =========================================================

points = np.array([
    [2,1],
    [3,1],
    [3,4],
    [2,4],
    [2,1]
], dtype=float)

labels = ["G","H","C","B"]

# =========================================================
# FIGURE
# =========================================================

fig, ax = plt.subplots(figsize=(8,8))

ax.set_xlim(-6,8)
ax.set_ylim(-6,6)

ax.set_aspect('equal')

ax.grid(True)

# =========================================================
# SUMBU
# =========================================================

ax.axhline(0,color='black',linewidth=2)
ax.axvline(0,color='black',linewidth=2)

# =========================================================
# GARIS CERMIN
# =========================================================

ax.axhline(
    y=0,
    color='purple',
    linestyle='--',
    linewidth=3
)

# =========================================================
# GARIS
# =========================================================

garis_asli, = ax.plot(
    [],
    [],
    'bo-',
    linewidth=3,
    markersize=8
)

garis_cermin, = ax.plot(
    [],
    [],
    'ro-',
    linewidth=3,
    markersize=8
)

# =========================================================
# LABEL
# =========================================================

label_asli = []
label_cermin = []

for _ in labels:

    t1 = ax.text(0,0,"",color='blue')
    t2 = ax.text(0,0,"",color='red')

    label_asli.append(t1)
    label_cermin.append(t2)

# =========================================================
# UPDATE
# =========================================================

def update(frame):

    gerak = np.sin(frame * 0.05) * 1.5

    objek = points.copy()
    objek[:,1] += gerak

    cermin = objek.copy()
    cermin[:,1] = -cermin[:,1]

    garis_asli.set_data(
        objek[:,0],
        objek[:,1]
    )

    garis_cermin.set_data(
        cermin[:,0],
        cermin[:,1]
    )

    for i,nama in enumerate(labels):

        x1 = objek[i,0]
        y1 = objek[i,1]

        label_asli[i].set_position(
            (x1+0.2,y1+0.2)
        )

        label_asli[i].set_text(
            f"{nama}"
        )

        x2 = cermin[i,0]
        y2 = cermin[i,1]

        label_cermin[i].set_position(
            (x2+0.2,y2-0.4)
        )

        label_cermin[i].set_text(
            f"{nama}'"
        )

    return (
        garis_asli,
        garis_cermin,
        *label_asli,
        *label_cermin
    )

# =========================================================
# ANIMASI
# =========================================================

animasi = FuncAnimation(
    fig,
    update,
    frames=200,
    interval=30,
    blit=True
)

# =========================================================
# SIMPAN GIF
# =========================================================

print("Membuat GIF...")

animasi.save(
    "cermin.gif",
    writer=PillowWriter(fps=30)
)

print("cermin.gif berhasil dibuat!")

plt.close()