# Name: Annafi Al Ghifari
# NIM: 2511533013
# Question 1
 
# bagian A
# text = "Informatika"
# print(text[9])
# print(text.upper())
# print(text[0:20])

# bagian B
text = "Annafi Al Ghifari"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)
