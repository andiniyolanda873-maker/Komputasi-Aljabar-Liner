import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =========================================================
# VISUALISASI TRANSFORMASI CERMIN TERHADAP SUMBU-X
# =========================================================
# Rumus:
# (x, y) -> (x, -y)
# =========================================================

# ---------------------------------------------------------
# TITIK OBJEK ASLI
# ---------------------------------------------------------

points = np.array([
    [2, 1],   # G
    [3, 1],   # H
    [3, 4],   # C
    [2, 4],   # B
    [2, 1]
], dtype=float)

labels = ["G", "H", "C", "B"]

# ---------------------------------------------------------
# MEMBUAT WINDOW
# ---------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 10))

# ---------------------------------------------------------
# PENGATURAN KOORDINAT
# ---------------------------------------------------------

ax.set_xlim(-6, 8)
ax.set_ylim(-6, 6)

ax.set_aspect('equal')

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)

# ---------------------------------------------------------
# SUMBU X DAN Y
# ---------------------------------------------------------

ax.axhline(0, color='black', linewidth=2)
ax.axvline(0, color='black', linewidth=2)

ax.set_xticks(np.arange(-6, 9, 1))
ax.set_yticks(np.arange(-6, 7, 1))

ax.text(7.2, 0.3, "SUMBU X", fontsize=12, fontweight='bold')
ax.text(0.3, 5.3, "SUMBU Y", fontsize=12, fontweight='bold')

# ---------------------------------------------------------
# GARIS CERMIN
# ---------------------------------------------------------

ax.axhline(
    y=0,
    color='purple',
    linestyle='--',
    linewidth=3,
    label='Garis Cermin'
)

# ---------------------------------------------------------
# GARIS OBJEK ASLI
# ---------------------------------------------------------

garis_asli, = ax.plot(
    [],
    [],
    'bo-',
    linewidth=3,
    markersize=9,
    label='Objek Asli'
)

# ---------------------------------------------------------
# GARIS BAYANGAN CERMIN
# ---------------------------------------------------------

garis_cermin, = ax.plot(
    [],
    [],
    'ro-',
    linewidth=3,
    markersize=9,
    label='Bayangan Cermin'
)

# ---------------------------------------------------------
# LABEL TITIK
# ---------------------------------------------------------

label_asli = []
label_cermin = []

for _ in labels:

    t1 = ax.text(
        0,
        0,
        "",
        fontsize=10,
        color='blue',
        fontweight='bold',
        bbox=dict(
            facecolor='white',
            edgecolor='blue',
            alpha=0.9
        )
    )

    t2 = ax.text(
        0,
        0,
        "",
        fontsize=10,
        color='red',
        fontweight='bold',
        bbox=dict(
            facecolor='white',
            edgecolor='red',
            alpha=0.9
        )
    )

    label_asli.append(t1)
    label_cermin.append(t2)

# ---------------------------------------------------------
# PANEL PENJELASAN
# ---------------------------------------------------------

penjelasan = fig.text(
    0.02,
    0.88,
    "",
    fontsize=11,
    verticalalignment='top',
    bbox=dict(
        facecolor='white',
        edgecolor='black',
        alpha=0.95
    )
)

# =========================================================
# FUNGSI ANIMASI
# =========================================================

def update(frame):

    # Gerakan naik turun
    gerak = np.sin(frame * 0.04) * 1.5

    # -----------------------------------------------------
    # OBJEK BERGERAK
    # -----------------------------------------------------

    objek = points.copy()
    objek[:, 1] += gerak

    # -----------------------------------------------------
    # TRANSFORMASI CERMIN
    # -----------------------------------------------------

    cermin = objek.copy()

    # Rumus pencerminan
    cermin[:, 1] = -cermin[:, 1]

    # -----------------------------------------------------
    # UPDATE GARIS
    # -----------------------------------------------------

    garis_asli.set_data(
        objek[:, 0],
        objek[:, 1]
    )

    garis_cermin.set_data(
        cermin[:, 0],
        cermin[:, 1]
    )

    # -----------------------------------------------------
    # UPDATE LABEL
    # -----------------------------------------------------

    for i, nama in enumerate(labels):

        # Titik asli
        x1 = objek[i, 0]
        y1 = objek[i, 1]

        label_asli[i].set_position(
            (x1 + 0.2, y1 + 0.2)
        )

        label_asli[i].set_text(
            f"{nama} ({x1:.1f}, {y1:.1f})"
        )

        # Titik bayangan
        x2 = cermin[i, 0]
        y2 = cermin[i, 1]

        label_cermin[i].set_position(
            (x2 + 0.2, y2 - 0.5)
        )

        label_cermin[i].set_text(
            f"{nama}' ({x2:.1f}, {y2:.1f})"
        )

    # -----------------------------------------------------
    # PANEL PENJELASAN
    # -----------------------------------------------------

    penjelasan.set_text(
        "TRANSFORMASI CERMIN TERHADAP SUMBU-X\n\n"
        "Rumus:\n"
        "(x, y) → (x, -y)\n\n"
        "Penjelasan:\n"
        "- Nilai x tetap\n"
        "- Nilai y berubah tanda\n"
        "- Bayangan simetris terhadap sumbu-X\n"
        "- Jarak terhadap sumbu-X tetap\n\n"
        "Keterangan:\n"
        "• Biru  = Objek Asli\n"
        "• Merah = Bayangan Cermin\n"
        "• Ungu  = Garis Cermin"
    )

    return (
        garis_asli,
        garis_cermin,
        *label_asli,
        *label_cermin
    )

# =========================================================
# MENJALANKAN ANIMASI
# =========================================================

animasi = FuncAnimation(
    fig,
    update,
    frames=1000,
    interval=20,
    blit=True
)

# ---------------------------------------------------------
# JUDUL
# ---------------------------------------------------------

plt.title(
    "Visualisasi Transformasi Cermin terhadap Sumbu-X",
    fontsize=15,
    fontweight='bold'
)

plt.legend(loc='lower right')

# =========================================================
# SIMPAN MENJADI GIF
# =========================================================

animasi.save(
    "cermin_sumbu_x.gif",
    writer="pillow",
    fps=30
)

# =========================================================
# TAMPILKAN
# =========================================================

plt.show()