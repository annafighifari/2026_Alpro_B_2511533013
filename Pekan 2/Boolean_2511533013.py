# Deklarasi variabel dengan tipe data Boolean
is_lulus_3013 = True
is_cumlaude_3013 = True

# Menggunakan Boolean
nilai_3013 = 85
batas_lulus_3013 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai_3013 >= batas_lulus_3013 #hasil akan true

print("=== Check Status Kelulusan ===")
print("Nilai:", nilai_3013)
print("Apakah lulus?", status_kelulusan)
if is_lulus_3013 and is_cumlaude_3013:
    print("Selamat! Anda lulus dengan predikat cumlaude.")