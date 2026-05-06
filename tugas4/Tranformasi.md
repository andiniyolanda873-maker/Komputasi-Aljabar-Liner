# Perhitungan Matriks Transformasi Geometri pada Bidang 2D

---

<iframe src="https://www.geogebra.org/calculator/gyrwvqbr?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

---

## Koordinat Titik yang akan kita hitung

Dari gambar pada bidang koordinat, kita bisa baca posisi tiap titik yaitu:

$$
A \to B
$$

$$
B \to C
$$

$$
D \to E
$$

$$
E \to F
$$

$$
A \to C
$$

$$
D \to F
$$

---

## Rumus yang akan di pakai buat menghitung Tranformasi

$$
x' = x + t_x
$$

$$
y' = y + t_y
$$

## Transformasi = $A \to B$

$$
A(2,3) \rightarrow B(2,1)
$$

$$
dx = 2 - 2 = 0
$$

$$
dy = 1 - 3 = -2
$$

$$
T =
\begin{bmatrix}
0 \\
-2
\end{bmatrix}
$$

---

## Transformasi = $B \to C$

$$
B(2,1) \rightarrow C(4,1)
$$

$$
dx = 4 - 2 = 2
$$

$$
dy = 1 - 1 = 0
$$

$$
T =
\begin{bmatrix}
2 \\
0
\end{bmatrix}
$$

---

## Transformasi = $D \to E$

$$
D(2,4) \rightarrow E(2,0)
$$

$$
dx = 2 - 2 = 0
$$

$$
dy = 0 - 4 = -4
$$

$$
T =
\begin{bmatrix}
0 \\
-4
\end{bmatrix}
$$

---

## Transformasi = $E \to F$

$$
E(2,0) \rightarrow F(4,0)
$$

$$
dx = 4 - 2 = 2
$$

$$
dy = 0 - 0 = 0
$$

$$
T =
\begin{bmatrix}
2 \\
0
\end{bmatrix}
$$

---

## Transformasi = $A \to C$

$$
A(2,3) \rightarrow C(4,1)
$$

$$
dx = 4 - 2 = 2
$$

$$
dy = 1 - 3 = -2
$$

$$
T =
\begin{bmatrix}
2 \\
-2
\end{bmatrix}
$$

---

## Transformasi = $D \to F$

$$
D(2,4) \rightarrow F(4,0)
$$

$$
dx = 4 - 2 = 2
$$

$$
dy = 0 - 4 = -4
$$

$$
T =
\begin{bmatrix}
2 \\
-4
\end{bmatrix}
$$

---

## Kesimpulan:

Semua perpindahan titik seperti $A \to B$, $B \to C$, $D \to E$, $E \to F$, $A \to C$, dan $D \to F$ merupakan translasi murni yang diperoleh dari selisih koordinat titik awal dan akhir, dimana arah pergeseran meliputi gerakan horizontal dan vertikal tanpa mengubah bentuk maupun ukuran objek, serta komposisi transformasi berurutan tetap konsisten dengan hasil transformasi langsung, namun karena besar translasi berbeda-beda maka tidak dapat direpresentasikan sebagai satu transformasi global melainkan bersifat lokal pada setiap pasangan titik.
