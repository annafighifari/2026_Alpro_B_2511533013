# Name: Annafi Al Ghifari
# NIM: 2511533013
# Question 1

phone = "082511533013"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)