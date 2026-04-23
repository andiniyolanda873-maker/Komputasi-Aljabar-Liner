<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Laporan Aljabar Linear</title>

<!-- MathJax -->
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<style>
body {
  font-family: Arial;
  margin: 40px;
  line-height: 1.6;
}
h1, h2 {
  text-align: center;
}
h2 {
  margin-top: 40px;
}
.section {
  margin-top: 30px;
}
</style>

</head>
<body>

<h1>Laporan Aljabar Linear</h1>
<p style="text-align:center;">Determinan dan Invers Matriks</p>

<!-- ================= NOMOR 1 ================= -->
<div class="section">
<h2>1. Determinan Matriks 2×2</h2>

$$
A=\begin{pmatrix}
-7 & -5\\
1 & 4
\end{pmatrix}
$$

$$
\det(A)=(-7)(4)-(-5)(1)=-28+5=-23
$$

<p>
Determinan dihitung dari selisih perkalian diagonal utama dan diagonal kedua.
Hasil negatif menunjukkan adanya perubahan orientasi pada transformasi.
</p>
</div>

<!-- ================= NOMOR 2 ================= -->
<div class="section">
<h2>2. Determinan Matriks 3×3</h2>

$$
A=\begin{pmatrix}
0 & 2 & -3\\
1 & -2 & -1\\
0 & 0 & 1
\end{pmatrix}
$$

$$
\det(A)=(-1)^{1+2}(2)
\begin{vmatrix}
1 & -1\\
0 & 1
\end{vmatrix}
=-2
$$

<p>
Menggunakan ekspansi kofaktor pada baris pertama.
Elemen nol membuat perhitungan lebih sederhana.
</p>
</div>

<!-- ================= NOMOR 3 ================= -->
<div class="section">
<h2>3. Determinan Matriks 4×4</h2>

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

<p>
Jumlah setiap baris sama dengan nol, sehingga baris saling bergantung.
Akibatnya determinan bernilai nol.
</p>
</div>

<!-- ================= NOMOR 4 ================= -->
<div class="section">
<h2>4. Invers Matriks 2×2</h2>

$$
A=\begin{pmatrix}
-7 & -5\\
1 & 4
\end{pmatrix}
$$

$$
\det(A)=-23
$$

$$
A^{-1}=\frac{1}{-23}
\begin{pmatrix}
4 & 5\\
-1 & -7
\end{pmatrix}
$$

<p>
Invers diperoleh dari adj(A) yang dibagi dengan determinan.
</p>
</div>

<!-- ================= NOMOR 5 ================= -->
<div class="section">
<h2>5. Invers Matriks 3×3</h2>

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

<p>
Adjoint diperoleh dari transpose matriks kofaktor.
</p>
</div>

<!-- ================= NOMOR 6 ================= -->
<div class="section">
<h2>6. Invers Matriks 4×4</h2>

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

<p>
Karena determinan nol, matriks tidak memiliki invers (singular).
</p>
</div>

</body>
</html>
