print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_3013 = int(input("Masukkan ukuran skala jam pasir (N): "))

print("#", end="")
for i_3013 in range(4 * n_3013 + 5):
    print("=", end="")
print("#")

for baris_3013 in range(n_3013, 0, -1):
    print("| ", end="")
    
    for spasi_kiri_3013 in range(2 * (n_3013 - baris_3013)):
        print(" ", end="")
        
    for angka_kiri_3013 in range(baris_3013, 0, -1):
        print(f"{angka_kiri_3013} ", end="")
        
    print("<*>", end="")
    
    for angka_kanan_3013 in range(1, baris_3013 + 1):
        print(f" {angka_kanan_3013}", end="")
        
    for spasi_kanan_3013 in range(2 * (n_3013 - baris_3013)):
        print(" ", end="")
        
    print(" |")

print("|", end="")
for spasi_poros_kiri_3013 in range(2 * n_3013 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_poros_kanan_3013 in range(2 * n_3013 + 1):
    print(" ", end="")
print("|")

for baris_3013 in range(1, n_3013 + 1):
    print("| ", end="")
    
    for spasi_kiri_3013 in range(2 * (n_3013 - baris_3013)):
        print(" ", end="")
        
    for angka_kiri_3013 in range(baris_3013, 0, -1):
        print(f"{angka_kiri_3013} ", end="")
        
    print("<*>", end="")
    
    for angka_kanan_3013 in range(1, baris_3013 + 1):
        print(f" {angka_kanan_3013}", end="")
        
    for spasi_kanan_3013 in range(2 * (n_3013 - baris_3013)):
        print(" ", end="")
        
    print(" |")

print("#", end="")
for i_3013 in range(4 * n_3013 + 5):
    print("=", end="")
print("#")