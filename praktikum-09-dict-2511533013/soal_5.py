n = int(input())
kas = {}

for _ in range(n):
    baris = input().split()
    nama = baris[0]
    nominal = int(baris[1])
    
    if nama in kas:
        kas[nama] += nominal
    else:
        kas[nama] = nominal

total_kas = 0
top_nama = ""
top_nominal = -1

for nama, total in kas.items():
    print(f"{nama}: {total}")
    total_kas += total
    if total > top_nominal:
        top_nominal = total
        top_nama = nama

print(f"Total cash: {total_kas}")
print(f"Top contributor: {top_nama} ({top_nominal})")