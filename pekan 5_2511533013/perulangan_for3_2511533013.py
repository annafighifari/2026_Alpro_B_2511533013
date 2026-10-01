ulang_3013 = int(input("Masukkan jumlah perulangan: "))

jumlah_3013 = 0
for i_3013 in range(1, ulang_3013 + 1):
    print(i_3013, end=" ")
    jumlah_3013 = jumlah_3013 + i_3013

    if i_3013 < ulang_3013:
        print("+", end=" ")
    else:
        print("=", jumlah_3013, end=" ")
print()
print("Jumlah =", jumlah_3013)