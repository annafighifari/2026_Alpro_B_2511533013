# program ini memakai fungsi input()
# program operator keanggotaan dan identitas

print("/n========================")
print("1. OPERATOR KEANGGOTAAN")
print("========================")

# input beberapa data_3013 yg dipisahkan dgn koma
input_data_3013 = input("masukkan beberapa angka, pisahkan dengan koma:")

# mengubah input menjadi list integer
data_3013 = [int(angka_3013.strip()) for angka_3013 in input_data_3013.split(",")]

nilai_dicari_3013 = int(input("Masukkan angka yang ingin dicari:"))

# operator in
hasil_3013 = nilai_dicari_3013 in data_3013

# operator not in
hasil_3013 = nilai_dicari_3013 not in data_3013
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3013, "not in", data_3013, "=", hasil_3013)

print("/n========================")
print("2. OPERATOR IDENTITAS")
print("========================")

# objek1 memakai list dari input pengguna
objek1_3013 = data_3013

# objek2 merujuk pada objek yang sama dengan objek1
objek2_3013 = data_3013

# objek3 memiliki isi sama, tapi merupakan objek baru
objek3_3013 = data_3013.copy()

print("objek1 =", objek1_3013)
print("objek2 =", objek2_3013)
print("objek3 =", objek3_3013)

# operator is
hasil_3013 = objek1_3013 is objek2_3013
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_3013)

# operator is not
hasil_3013 = objek1_3013 is objek2_3013
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_3013)

# membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_3013 is objek3_3013)
print("objek1 == objek3 =", objek1_3013 == objek3_3013)
