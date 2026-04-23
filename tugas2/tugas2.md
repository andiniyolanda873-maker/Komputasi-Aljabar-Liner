# Tugas 3

## A. Hitunglah determinan matrik berikut dengan menggunakan rumus expansi baris

## 1.

$$
A=\begin{pmatrix}
-7 & -5\\
1 & 4
\end{pmatrix}
$$

$$
\det(A)=(-1)^{1+1}(-7)\begin{vmatrix}4\end{vmatrix}
+(-1)^{1+2}(-5)\begin{vmatrix}1\end{vmatrix}
$$

$$
= (-7)(4) - (-5)(1)
= -28 + 5
= -23
$$

##

## 2

$$
A=\begin{pmatrix}
0 & 2 & -3\\
1 & -2 & -1\\
0 & 0 & 1
\end{pmatrix}
$$

$$
\det(A)=(-1)^{1+1}(0)\begin{vmatrix}-2 & -1\\0 & 1\end{vmatrix}
+(-1)^{1+2}(2)\begin{vmatrix}1 & -1\\0 & 1\end{vmatrix}
+(-1)^{1+3}(-3)\begin{vmatrix}1 & -2\\0 & 0\end{vmatrix}
$$

$$
= 0 - 2(1) + (-3)(0)
= -2
$$

##

## 3

$$
A=\begin{pmatrix}
1 & -3 & 1 & 1\\
-3 & 1 & 1 & 1\\
1 & 1 & -3 & 1\\
1 & 1 & 1 & -3
\end{pmatrix}
$$

$$
\det(A)=
(+1)\begin{vmatrix}
1 & 1 & 1\\
1 & -3 & 1\\
1 & 1 & -3
\end{vmatrix}
-(-3)\begin{vmatrix}
-3 & 1 & 1\\
1 & -3 & 1\\
1 & 1 & -3
\end{vmatrix}
$$

$$
+1\begin{vmatrix}
-3 & 1 & 1\\
1 & 1 & 1\\
1 & 1 & -3
\end{vmatrix}
-1\begin{vmatrix}
-3 & 1 & 1\\
1 & 1 & -3\\
1 & 1 & 1
\end{vmatrix}
$$

$$
= 16 - 48 + 16 + 16
= 0
$$

1. ## Matriks 2x2
   Determinan 2×2 berasal dari konsep luas (area scaling), sehingga rumusnya sederhana: perkalian diagonal utama dikurangi diagonal kedua.
   Tidak ada kofaktor kompleks di sini, tapi ini sebenarnya bentuk paling dasar dari ekspansi kofaktor.
   Tanda negatif muncul karena ada “arah” (orientasi) dalam perkalian silang tersebut.
   Kesalahan yang sering terjadi: lupa bahwa minus ketemu minus jadi plus.
   Hasil −23 menunjukkan transformasi matriks membalik orientasi (karena negatif) dan mengubah skala sebesar 23.
2. ## Matriks 3x3
   Ekspansi kofaktor (Aij) berarti kita memecah determinan jadi kombinasi determinan 2×2 (minor).
   Pemilihan baris pertama bukan wajib, tapi strategis karena ada elemen 0 → mengurangi beban hitung.
   Tanda kofaktor mengikuti pola papan catur (+ − +), ini krusial karena sering jadi sumber kesalahan.
   Minor yang mengandung baris nol menghasilkan determinan 0, sehingga langsung menghilangkan kontribusi.
   Hasil −2 menunjukkan matriks masih invertible (tidak singular), tapi skala transformasinya kecil dan membalik orientasi.
3. ## Matriks 4x4
   Secara prosedur, ekspansi kofaktor akan memecah jadi empat determinan 3×3, lalu masing-masing dipecah lagi → ini cepat jadi panjang.
   Namun terlihat pola simetris: diagonal −3 dan elemen lain 1 → ini memberi petunjuk struktur khusus.
   Jika jumlah setiap baris = 0, berarti ada ketergantungan linear (salah satu baris bisa dibentuk dari yang lain).
   Ketergantungan linear ⇒ volume ruang hasil transformasi = 0 ⇒ determinan = 0.
   Jadi meskipun secara hitungan panjang bisa dibuktikan, secara konsep kita sudah tahu hasilnya pasti 0 tanpa ekspansi penuh.

## B. Gunakan rumus matriks adjoin untuk menghitung invers dari matriks berikut dengan rumus

## 4.

$$
A=\begin{pmatrix}
-7 & -5\\
1 & 4
\end{pmatrix}
$$

$$
\det(A)=(-7)(4)-(-5)(1)=-28+5=-23
$$

$$
\operatorname{adj}(A)=
\begin{pmatrix}
4 & 5\\
-1 & -7
\end{pmatrix}
$$

$$
A^{-1}=\frac{1}{-23}
\begin{pmatrix}
4 & 5\\
-1 & -7
\end{pmatrix}
$$

## 5.

$$
A=\begin{pmatrix}
0 & 2 & -3\\
1 & -2 & -1\\
0 & 0 & 1
\end{pmatrix}
$$

$$
\det(A)=-2
$$

$$
\text{Kofaktor:}
$$

$$
A_{11}=
\begin{vmatrix}
-2 & -1\\
0 & 1
\end{vmatrix}=-2,\quad
A_{12}=-
\begin{vmatrix}
2 & -3\\
0 & 1
\end{vmatrix}=-2,\quad
A_{13}=
\begin{vmatrix}
2 & -3\\
-2 & -1
\end{vmatrix}=-8
$$

$$
A_{21}=-
\begin{vmatrix}
1 & -1\\
0 & 1
\end{vmatrix}=-1,\quad
A_{22}=
\begin{vmatrix}
0 & -3\\
0 & 1
\end{vmatrix}=0,\quad
A_{23}=-
\begin{vmatrix}
0 & -3\\
1 & -1
\end{vmatrix}=3
$$

$$
A_{31}=
\begin{vmatrix}
1 & -2\\
0 & 0
\end{vmatrix}=0,\quad
A_{32}=-
\begin{vmatrix}
0 & -3\\
1 & -1
\end{vmatrix}=3,\quad
A_{33}=
\begin{vmatrix}
0 & 2\\
1 & -2
\end{vmatrix}=-2
$$

$$
\operatorname{adj}(A)=
\begin{pmatrix}
-2 & -2 & -8\\
-1 & 0 & 3\\
0 & 3 & -2
\end{pmatrix}
$$

$$
A^{-1}=\frac{1}{-2}\operatorname{adj}(A)
$$

## 6.

$$
A=\begin{pmatrix}
1 & -3 & 1 & 1\\
-3 & 1 & 1 & 1\\
1 & 1 & -3 & 1\\
1 & 1 & 1 & -3
\end{pmatrix}
$$

$$
\det(A)=0
$$

$$
A^{-1}\ \text{tidak ada}
$$

4. ## Invers matriks 2×2 tetap mengikuti rumus umum: hanya saja bentuk adjoint-nya lebih sederhana (tukar diagonal, ubah tanda elemen luar).

   Determinan wajib dihitung di awal karena menjadi pembagi; kalau salah di sini, semua hasil ikut salah.
   adj(A) berasal dari kofaktor lalu transpose, meskipun pada 2×2 terlihat seperti “langsung jadi”.
   Karena determinan ≠ 0, matriks pasti memiliki invers (tidak singular).

5. ## Proses utama ada di pembentukan kofaktor, yaitu menghitung minor 2×2 lalu memberi tanda sesuai pola (+ − + / − + − / + − +).

   adj(A) diperoleh dari transpose matriks kofaktor, jadi posisi elemen berubah (ini sering jadi sumber kesalahan).
   Determinan = −2 memastikan matriks bisa diinverskan dan menjadi faktor pembagi.
   Struktur matriks yang punya banyak nol sebenarnya membantu mempercepat perhitungan minor.

6. ## Langkah awal tetap sama: cek determinan sebelum lanjut ke adjoint.
   Hasil determinan = 0 menunjukkan adanya ketergantungan linear antar baris.
   Karena rumus invers membagi dengan determinan, maka pembagian tidak bisa dilakukan.
   Akibatnya, meskipun adj(A) bisa saja dihitung, invers matriks tidak ada (singular).
