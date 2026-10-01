tinggi_3013 = int(input("Masukkan tinggi piramida: "))

for i_3013 in range(1, tinggi_3013 + 1):
    spasi_3013 = " " * (tinggi_3013 - i_3013)
    bintang_3013 = "*" * (2 * i_3013 - 1)

    print(spasi_3013 + bintang_3013)