#Perhitungan Matriks Transformasi Geometri pada Bidang 2D\*\*

### Menggunakan Metode Aljabar Linear & Koordinat Homogen

---

## Koordinat Titik yang akan kita hitung

Dari gambar pada bidang koordinat, kita bisa baca posisi tiap titik yaitu:

$$
A = (1,\ 3), \quad
B = (1,\ 1), \quad
C = (4,\ 1), \quad
D = (1,\ 4), \quad
E = (1,\ 0), \quad
F = (4,\ 0)
$$

## Dalam konsep Dasar Matriks Transformasi

Suatu perpindahan atau perubahan posisi suatu titik di bidang 2D bisa direpresentasikan menggunakan matriks.  
Misalnya titik $P = (x,\ y)$ dipindahkan menjadi $P' = (x',\ y')$, maka hubungannya bisa ditulis seperti ini:

$$
\begin{bmatrix} x' \\ y' \end{bmatrix}
=
M \cdot \begin{bmatrix} x \\ y \end{bmatrix}
+
\begin{bmatrix} t_x \\ t_y \end{bmatrix}
$$

Di sini:

- $M$ adalah matriks transformasi (untuk rotasi, skala)
- $\mathbf{t} = (t_x,\ t_y)$ adalah vektor translasi atau bisa disebut (pergeseran)

Kalau hanya terjadi **translasi murni** (tidak ada rotasi atau perubahan ukuran), maka matriksnya jadi matriks identitas:

$$
\begin{bmatrix} x' \\ y' \end{bmatrix}
=
\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
+
\begin{bmatrix} t_x \\ t_y \end{bmatrix}
=
\begin{bmatrix} x + t_x \\ y + t_y \end{bmatrix}
$$

### Koordinat Homogen ($3 \times 3$)

Supaya semua jenis transformasi bisa digabung dalam satu operasi, kita pakai koordinat homogen.  
Caranya dengan menambahkan angka 1 di belakang, jadi $\tilde{P} = (x,\ y,\ 1)^\top$.

Dengan cara ini, translasi juga bisa ditulis dalam bentuk perkalian matriks yang nantinya kita kerjakan:

$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}
=
\underbrace{\begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix}}_{T}
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

---

## Transformasi 1 = $A \to B$

**Titik awal:** $A = (1,\ 3)$  
**Titik tujuan:** $B = (1,\ 1)$

### Menentukan Vektor Translasi

Kita cari selisihnya terlebih dahulu yaitu di posisi dari A ke B:

$$
t_x = x_B - x_A = 1 - 1 = 0
\qquad
t_y = y_B - y_A = 1 - 3 = -2
$$

Artinya titik digeser turun 2 satuan.

### Matriks Translasi $T_1$

$$
T_1 =
\begin{bmatrix}
1 & 0 &  0 \\
0 & 1 & -2 \\
0 & 0 &  1
\end{bmatrix}
$$

### Perhitungan

$$
T_1 \cdot \tilde{A} =
\begin{bmatrix}
1 & 0 &  0 \\
0 & 1 & -2 \\
0 & 0 &  1
\end{bmatrix}
\begin{bmatrix} 1 \\ 3 \\ 1 \end{bmatrix}
=
\begin{bmatrix}
1(1) + 0(3) + 0(1) \\
0(1) + 1(3) + (-2)(1) \\
0(1) + 0(3) + 1(1)
\end{bmatrix}
=
\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}
= \tilde{B} \quad \checkmark
$$

---

## Transformasi 2 = $B \to C$

**Titik awal:** $B = (1,\ 1)$  
**Titik tujuan:** $C = (4,\ 1)$

### Menentukan Vektor Translasi

$$
t_x = x_C - x_B = 4 - 1 = 3
\qquad
t_y = y_C - y_B = 1 - 1 = 0
$$

Artinya titik digeser ke kanan 3 satuan.

### Matriks Translasi $T_2$

$$
T_2 =
\begin{bmatrix}
1 & 0 & 3 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

### Perhitungan

$$
T_2 \cdot \tilde{B} =
\begin{bmatrix}
1 & 0 & 3 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}
=
\begin{bmatrix}
1(1) + 0(1) + 3(1) \\
0(1) + 1(1) + 0(1) \\
0(1) + 0(1) + 1(1)
\end{bmatrix}
=
\begin{bmatrix} 4 \\ 1 \\ 1 \end{bmatrix}
= \tilde{C} \quad \checkmark
$$

---

## Transformasi 3 = $D \to E$

**Titik awal:** $D = (1,\ 4)$  
**Titik tujuan:** $E = (1,\ 0)$

### Menentukan Vektor Translasi

$$
t_x = x_E - x_D = 1 - 1 = 0
\qquad
t_y = y_E - y_D = 0 - 4 = -4
$$

Artinya titik turun 4 satuan.

### Matriks Translasi $T_3$

$$
T_3 =
\begin{bmatrix}
1 & 0 &  0 \\
0 & 1 & -4 \\
0 & 0 &  1
\end{bmatrix}
$$

### Perhitungan

$$
T_3 \cdot \tilde{D} =
\begin{bmatrix}
1 & 0 &  0 \\
0 & 1 & -4 \\
0 & 0 &  1
\end{bmatrix}
\begin{bmatrix} 1 \\ 4 \\ 1 \end{bmatrix}
=
\begin{bmatrix}
1(1) + 0(4) + 0(1) \\
0(1) + 1(4) + (-4)(1) \\
0(1) + 0(4) + 1(1)
\end{bmatrix}
=
\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}
= \tilde{E} \quad \checkmark
$$

---

## Transformasi 4 = $E \to F$

**Titik awal:** $E = (1,\ 0)$  
**Titik tujuan:** $F = (4,\ 0)$

### Menentukan Vektor Translasi

$$
t_x = x_F - x_E = 4 - 1 = 3
\qquad
t_y = y_F - y_E = 0 - 0 = 0
$$

Artinya titik digeser ke kanan 3 satuan.

### Matriks Translasi $T_4$

$$
T_4 =
\begin{bmatrix}
1 & 0 & 3 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

### Perhitungan

$$
T_4 \cdot \tilde{E} =
\begin{bmatrix}
1 & 0 & 3 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}
=
\begin{bmatrix}
1(1) + 0(0) + 3(1) \\
0(1) + 1(0) + 0(1) \\
0(1) + 0(0) + 1(1)
\end{bmatrix}
=
\begin{bmatrix} 4 \\ 0 \\ 1 \end{bmatrix}
= \tilde{F} \quad \checkmark
$$

---

## Ringkasan dari perhitungan Matriks Tranformasi dari awal sampe akhir

### 1. Dari $A(1,3)$ ke $B(1,1)$

Translasi: $(0,\ -2)$

$$
\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{bmatrix}
$$

---

### 2. Dari $B(1,1)$ ke $C(4,1)$

Translasi: $(+3,\ 0)$

$$
\begin{bmatrix} 1 & 0 & 3 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

---

### 3. Dari $D(1,4)$ ke $E(1,0)$

Translasi: $(0,\ -4)$

$$
\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & -4 \\ 0 & 0 & 1 \end{bmatrix}
$$

---

### 4. Dari $E(1,0)$ ke $F(4,0)$

Translasi: $(+3,\ 0)$

$$
\begin{bmatrix} 1 & 0 & 3 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

---

## Analisis Transformasi Gabungan

Secara teori, transformasi-transformasi yang telah diperoleh dapat digabungkan dalam bentuk komposisi matriks:

$$
T_{total} = T_4 \cdot T_3 \cdot T_2 \cdot T_1
$$

Berdasarkan hasil perhitungan, setiap pasangan titik memiliki nilai translasi yang berbeda, yaitu:

$$
A \to B = (0, -2)
$$

$$
B \to C = (3, 0)
$$

$$
D \to E = (0, -4)
$$

$$
E \to F = (3, 0)
$$

Karena besar translasi tidak sama, maka tdak dapat dibentuk satu matriks transformasi tunggal Komposisi matriks hanya berlaku untuk urutan tertentu (misalnya $A \to B \to C$)
Transformasi bersifat lokal, bukan global

---

**Kesimpulan:**
Dari proses di atas dapat disimpulkan bahwa perpindahan titik-titik pada bidang 2D dimodelkan menggunakan transformasi translasi yang ditentukan dari selisih koordinat awal dan akhir, dimana semua transformasi yang terjadi merupakan translasi murni sehingga tidak mengubah bentuk dan ukuran objek, serta dengan memanfaatkan koordinat homogen seluruh transformasi dapat dituliskan dalam bentuk matriks yang seragam sehingga lebih sederhana untuk dihitung, digabung, dan diterapkan.
