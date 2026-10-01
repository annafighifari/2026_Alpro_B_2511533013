tinggi_3013 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3013 % 2 != 0:
    print("Tinggi pola harus bilangan genap.")
else:
    a_3013 = tinggi_3013 
    c_3013 = a_3013
    lebar_3013 = (2 * tinggi_3013) - 2

    for i_3013 in range(1, tinggi_3013 + 1):
        b_3013 = c_3013 + 1

        for j_3013 in range(1, lebar_3013 + 1):

            # baris atas dan bawah
            if i_3013 == 1 or i_3013 == tinggi_3013:
                if j_3013 == 1 or j_3013 == lebar_3013:
                    print("#", end="")
                else:
                    print("=", end="")
                    # baris isi
            else:
                if j_3013 == 1 or j_3013 == lebar_3013:
                    print("|", end="")
                else:
                    if j_3013 == c_3013:
                        print("<", end="")
                    elif j_3013 == b_3013:
                        print(">", end="")
                    elif j_3013 == (lebar_3013 - c_3013):
                        print("<", end="")
                    elif j_3013 == (lebar_3013 - c_3013 + 1):
                        print(">", end="")
                    elif j_3013 > b_3013 and j_3013 < (lebar_3013 - c_3013):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()
        # logic asli java
        a_3013 -= 2
        if a_3013<= 0:
            c_3013 = (-a_3013) + 2
        else:
            c_3013 = a_3013  