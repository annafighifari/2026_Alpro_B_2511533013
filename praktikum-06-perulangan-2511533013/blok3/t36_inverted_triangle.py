# File: t36_inverted_triangle.py

# Meminta input tinggi dari pengguna
tinggi = int(input("Masukkan tinggi segitiga: "))

# Menampilkan segitiga terbalik
for i in range(tinggi, 0, -1):
    print("*" * i)