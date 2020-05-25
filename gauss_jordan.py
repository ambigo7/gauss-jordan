# MengImport Library Numpy
import numpy as np
import sys

# Menginput jumlah matrix yang tidak diketahui
n = int(input('Masukan jumlah Data: '))

# Membuat array numpy ukuran n x n + 1 dan menginisialisasi 
a = np.zeros((n,n+1))

# Membuat array numpy ukuran n dan menginisialisasi
# ke nol untuk menyimpan vektor solusi
x = np.zeros(n)

# Membaca koefisien matriks yang diperbesar
print('Masukan Data Matrixnya:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

print("Soal yang dimasukan :")
print(a)

# Menerapkan Eliminasi Gauss Jordan
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Dibagi dengan nol terdeteksi!')
        
    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

# Memperoleh Solusi
print("\n")
print("Eliminasi Gauss Jordan :")
print(a)

for i in range(n):
    x[i] = a[i][n]/a[i][i]

# Hasil Solusinya
print('\nSolusi yang diperlukan adalah: ')
print(" x,y,z =[{}]".format(x))