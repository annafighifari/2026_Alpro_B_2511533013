print("=== SISTEM TRANSAKSI TOKO ===\n")

# 1. INPUT DATA PELANGGAN DAN TRANSAKSI
nama_3013 = input("Masukkan Nama Pelanggan : ")
status_3013 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_belanja_3013 = float(input("Masukkan Total Belanja : "))
jumlah_barang_3013 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3013 = input("Masukkan Kode Promo : ").strip().upper()

# DAFTAR PROMO UNTUK OPERATOR MEMBERSHIP
daftar_promo_3013 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# 2. OPERATOR PERBANDINGAN & LOGIKA
is_min_belanja_3013 = total_belanja_3013 >= 200000
is_min_barang_3013 = jumlah_barang_3013 >= 3
is_member_3013 = status_3013 == "member"

promo_tersedia_3013 = kode_promo_3013 in daftar_promo_3013
promo_tidak_ada_3013 = kode_promo_3013 not in daftar_promo_3013

dapat_diskon_3013 = is_member_3013 and is_min_belanja_3013
dapat_promo_3013 = (is_min_barang_3013 or promo_tersedia_3013) and not promo_tidak_ada_3013

# 3. OPERATOR ARITMATIKA & ASSIGNMENT
persen_diskon_3013 = 0.10 if dapat_diskon_3013 else 0.0

besarnya_diskon_3013 = total_belanja_3013 * persen_diskon_3013
total_pembayaran_3013 = total_belanja_3013 - besarnya_diskon_3013
rata_rata_harga_3013 = total_belanja_3013 / jumlah_barang_3013
sisa_pembagian_3013 = jumlah_barang_3013 % 2  # Cek jumlah barang ganjil/genap

poin_3013 = 0
if dapat_promo_3013:
    poin_3013 += 50
    total_pembayaran_3013 -= 5000  # Potongan promo tambahan Rp5.000

# 4. OPERATOR IDENTITAS (is, is not)
objek_a_3013 = status_3013
objek_b_3013 = status_3013
objek_c_3013 = input_status_copy_3013 = str(status_3013)

cek_is_3013 = objek_a_3013 is objek_b_3013
cek_is_not_3013 = objek_a_3013 is not objek_c_3013

# 5. OPERATOR BITWISE
bit_member_3013 = 0b0001 if is_member_3013 else 0b0000
bit_belanja_3013 = 0b0010 if is_min_belanja_3013 else 0b0000
bit_barang_3013 = 0b0100 if is_min_barang_3013 else 0b0000
bit_promo_3013 = 0b1000 if promo_tersedia_3013 else 0b0000

status_biner_3013 = bit_member_3013 | bit_belanja_3013 | bit_barang_3013 | bit_promo_3013

cek_member_bitwise_3013 = status_biner_3013 & 0b0001
cek_promo_bitwise_3013 = status_biner_3013 & 0b1000

kode_referensi_3013 = 0b1011
perbandingan_xor_3013 = status_biner_3013 ^ kode_referensi_3013

geser_kiri_3013 = status_biner_3013 << 1

# OUTPUT UTAMA PROGRAM
print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan        : {nama_3013}")
print(f"Status Pelanggan      : {status_3013}")
print(f"Total Belanja         : Rp{total_belanja_3013:.0f}")
print(f"Jumlah Barang         : {jumlah_barang_3013}")
print(f"Kode Promo            : {kode_promo_3013}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000   : {is_min_belanja_3013}")
print(f"Jumlah Barang >= 3    : {is_min_barang_3013}")
print(f"Status Member         : {is_member_3013}")
print(f"Kode Promo Tersedia   : {promo_tersedia_3013}")
print(f"Mendapatkan Diskon    : {dapat_diskon_3013}")
print(f"Mendapatkan Promo     : {dapat_promo_3013}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                : Rp{besarnya_diskon_3013:.0f}")
print(f"Total Pembayaran      : Rp{total_pembayaran_3013:.0f}")
print(f"Rata-rata Harga Barang: Rp{rata_rata_harga_3013:.2f}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses        : {bin(status_biner_3013)[2:].zfill(4)}")
print(f"Member Access         : {bool(cek_member_bitwise_3013)}")
print(f"Promo Access          : {bool(cek_promo_bitwise_3013)}")
print(f"Free Shipping Access  : {kode_promo_3013 == 'GRATISONGKIR'}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner    : {bin(status_biner_3013)[2:].zfill(4)}")
print(f"Kode Desimal  : {status_biner_3013}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{bin(status_biner_3013)[2:].zfill(4)} & 0001")
print(f"Hasil Biner   : {bin(cek_member_bitwise_3013)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_member_bitwise_3013}")

print("\nCek Promo")
print(f"{bin(status_biner_3013)[2:].zfill(4)} & 1000")
print(f"Hasil Biner   : {bin(cek_promo_bitwise_3013)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_promo_bitwise_3013}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {bin(status_biner_3013)[2:].zfill(4)}")
print(f"Kode Referensi : {bin(kode_referensi_3013)[2:].zfill(4)}")
print(f"{bin(status_biner_3013)[2:].zfill(4)} ^ {bin(kode_referensi_3013)[2:].zfill(4)}")
print(f"Hasil Biner   : {bin(perbandingan_xor_3013)[2:].zfill(4)}")
print(f"Hasil Desimal : {perbandingan_xor_3013}")

print("\n=== Shift ===")
print(f"{bin(status_biner_3013)[2:].zfill(4)} << 1")
print(f"Hasil Biner   : {bin(geser_kiri_3013)[2:].zfill(5)}")
print(f"Hasil Desimal : {geser_kiri_3013}")

print("\n=== SELESAI ===")