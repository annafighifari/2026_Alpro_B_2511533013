# program ini menggunakan fungsi input()
# program operator logika dalam python

# memasukkan nilai boolean
# input tidak peka terhadap huruf kapital dan kecil
a1_3013 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_3013 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 =", a1_3013)
print("A2 =", a2_3013)

# konjungsi: bernailai True juka keduanya True
hasil_3013 = a1_3013 and a2_3013
print("\nOperator Konjungsi (AND)")
print("A1 and A2 =", hasil_3013)

# disjungsi: bernilai True jika salah satu True
hasil_3013 = a1_3013 or a2_3013
print("\nOperator Disjungsi (OR)")
print("A1 or A2 =", hasil_3013)

#  Negasi A1: membalik nilai A1
hasil_3013 = not a1_3013
print("\nOperator A1 (NOT)")
print("not A1 =", hasil_3013)

# Negasi A2: membalik nilai A2
hasil_3013 = not a2_3013
print("\nOperator A2 (NOT)")
print("not A2 =", hasil_3013)

# XOR: bernilai True jika kedua nilai berbeda
hasil_3013 = a1_3013 != a2_3013
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2 =", hasil_3013)
