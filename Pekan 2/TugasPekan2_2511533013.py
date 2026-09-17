from typing import Final

BATAS_LULUS_3013: Final[float] = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_3013 = input("Masukkan Nama Mahasiswa : ")
jk_3013 = input("Masukkan Jenis Kelamin (L/P): ")

print("Masukkan Alamat Domisili ( Tulis alamat lengkap):")
alamat_3013 = input()

umur_3013 = int(input("Masukkan Umur : "))
skor_3013 = float(input("Masukkan Skor Tes Awal : "))

token_3013 = complex(100, 3)

is_lulus_3013 = skor_3013 >= BATAS_LULUS_3013


print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa : {nama_3013} | Tipe: {type(nama_3013)}")
print(f"Jenis Kelamin : {jk_3013} | Tipe: {type(jk_3013)}")
print(f"Alamat Domisili:\n{alamat_3013} | Tipe: {type(alamat_3013)}")
print(f"Umur : {umur_3013} tahun | Tipe: {type(umur_3013)}")
print(f"Skor Tes Awal : {skor_3013} | Tipe: {type(skor_3013)}")
print(f"ID Token Sinyal: {token_3013} | Tipe: {type(token_3013)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {BATAS_LULUS_3013}")
print(f"Apakah Dinyatakan Lulus?: {is_lulus_3013} | Tipe: {type(is_lulus_3013)}")