# input dari user
total_belanja_3013 = float(input("Masukkan total belanja (Rp): "))

# input status member (cek apakah user mengetik 'y' atau 'ya')
input_member_3013 = input("Apakah anda member? (y/t): ").strip().lower()
is_member_3013 = input_member_3013 in ["y","ya"]

# input status kode promo (cek apakah user mengetik 'y' atau 'ya')
input_promo_3013 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3013 = input_promo_3013 in ["y","ya"]

total_diskon_persen_3013 = 0

if total_belanja_3013 > 1000000:
    total_diskon_persen_3013 += 10 #diskon belanja besar

if is_member_3013:
    total_diskon_persen_3013 += 5 #diskon member

if kode_promo_valid_3013:
    total_diskon_persen_3013 += 15 #diskon voucher

    # menghitung nominal diskon dan total bayar
    nominal_diskon_3013 = total_belanja_3013 + (total_diskon_persen_3013 / 100)
    total_bayar_3013 = total_belanja_3013 - nominal_diskon_3013

    # output hasil
    print("\n--- Rincian Pembayaran ---")
    print(f"Total Diskon    : (total_diskon_persen_3013)% (Rp {nominal_diskon_3013:,.0f})")
    print(f"Total Bayar     : Rp (total_bayar_3013:,.0f)") 

    print(f"Total diskon yang anda dapatkan: {total_diskon_persen_3013}%")
        #   output: total diskon yg anda dapatkan: 30% jika belanja > 1 juta, member dan kode promo valid