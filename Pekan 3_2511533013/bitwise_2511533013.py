# program ini menggunakan fungsi input()

print("\n========================")
print("3. OPERATOR BITWISE")
print("========================")

angka1_3013 = int(input("Masukkan angka bitwise-1: "))
angka2_3013 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_3013, "| biner =", bin(angka1_3013))
print("angka2 =", angka2_3013, "| biner =", bin(angka2_3013))

# bitwise AND
hasil_3013 = angka1_3013 & angka2_3013
print("\nBitwise AND (&)")
print(angka1_3013, "&", angka2_3013, "=", hasil_3013)
print("Biner hasil =", bin(hasil_3013))
print("Biner hasil (8 bit) =", format(hasil_3013, "08b"))

# bitwise XOR
hasil_3013 = angka1_3013 ^ angka2_3013
print("\nBitwise XOR (^)")
print(angka1_3013, "^", angka2_3013, "=", hasil_3013)
print("Biner hasil =", bin(hasil_3013))
print("Biner hasil (8 bit) =", format(hasil_3013, "08b"))

# bitwise NOT
hasil_3013 = ~angka1_3013
print("\nBitwise NOT (~)")
print("~", angka1_3013, "=", hasil_3013)
print("Biner hasil =", bin(hasil_3013))
print("Biner hasil (8 bit) =", format(hasil_3013, "08b"))

# bitwise geser kiri
jumlah_geser_3013 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3013 = angka1_3013 << jumlah_geser_3013
print("\nBitwise geser kanan (<<)")
print(angka1_3013, "<<", jumlah_geser_3013, "=", hasil_3013)
print("Biner hasil =", bin(hasil_3013))
print("Biner hasil (8 bit) =", format(hasil_3013, "08b"))

# bitwise geser kanan
hasil_3013 = angka1_3013 >> jumlah_geser_3013
print("\nBitwise geser kanan (>>)")
print(angka1_3013, ">>", jumlah_geser_3013, "=", hasil_3013)
print("Biner hasil =", bin(hasil_3013))
print("Biner hasil (8 bit) =", format(hasil_3013, "08b"))