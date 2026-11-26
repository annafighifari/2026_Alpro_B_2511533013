# Nama: Annafi Al Ghifari
# NIM: 2511533013
# Bonus

text = input("Kalimat: ")

# Hilangkan spasi dan ubah ke huruf kecil
clean = text.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")