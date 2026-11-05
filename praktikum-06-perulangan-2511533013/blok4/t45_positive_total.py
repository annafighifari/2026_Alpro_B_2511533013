total = 0

while True:
    num = int(input("Enter a number: "))
    
    if num < 0:
        break  # Bilangan negatif menghentikan loop
    elif num == 0:
        continue  # Bilangan 0 dilewati (kembali ke awal loop)
    
    print("Positive number:", num)
    total += num

print("Total:", total)