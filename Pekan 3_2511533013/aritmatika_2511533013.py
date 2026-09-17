angka1_3013 = int(input("Input angka-1: "))
angka2_3013 = int(input("Input angka-2: "))

# penjumlahan
hasil_3013 = angka1_3013 + angka2_3013
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3013)

# pengurangan
hasil_3013 = angka1_3013 - angka2_3013
print("\nOperator Pengurangan")
print("Hasil =", hasil_3013)

# perkalian
hasil_3013 = angka1_3013 * angka2_3013
print("\nOperator Perkalian")
print("Hasil =", hasil_3013)

# pembagian, pembagian bulat, dan sisa bagi
if angka2_3013 != 0:
    hasil_3013 = angka1_3013 / angka2_3013
    print("\nOperator Pembagian")
    print("Hasil =", hasil_3013)

    hasil_3013 = angka1_3013 // angka2_3013
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_3013)

    hasil_3013 = angka1_3013 % angka2_3013
    print("\nOperator Sisa bagi")
    print("Hasil =", hasil_3013)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# pangkat
hasil_3013 = angka1_3013 ** angka2_3013
print("\nOperator Pangkat")
print("Hasil =", hasil_3013)
