# program menggunakan fungsi input()
# nilai yang dimasukkan akan dikonversi menjadi tipedata integer
# program operator assignment dalam python

angka1_3013 = int(input("Input angka-1: "))
angka2_3013 = int(input("Input angka-2: "))

print("\nNilai awal angka1_3013=", angka1_3013)
print("\nNilai angka2=", angka2_3013)

# assignment biasa
hasil_3013 = angka1_3013
print("\nAssignment biasa (=)")
print("Hasil =", hasil_3013)

# Assignment penambahan
hasil_3013 = angka1_3013
hasil_3013 += angka2_3013
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_3013)

# Assignment pengurangan
hasil_3013 = angka1_3013
hasil_3013 -= angka2_3013
print("\nAssignment pengurangan (-=)")
print("Hasil_3013 =", hasil_3013)

# Assignment perkalian
hasil_3013 = angka1_3013
hasil_3013 *= angka2_3013
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_3013)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3013 != 0:
    hasil_3013 = angka1_3013
    hasil_3013 /= angka2_3013
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_3013)
    # operator tambahan
    hasil_3013 = angka1_3013
    hasil_3013 //= angka2_3013
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_3013)
    hasil_3013 = angka1_3013
    hasil_3013 %= angka2_3013
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_3013)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0")

# Operator tambahan: assignment perpangkatan
hasil_3013 = angka1_3013
hasil_3013 **= angka2_3013
print("\nAssignment perpangkatan (**=)")
print("hasil =", hasil_3013)