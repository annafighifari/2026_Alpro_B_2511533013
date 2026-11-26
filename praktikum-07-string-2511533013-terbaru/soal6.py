# Name: Annafi Al Ghifari
# NIM: 2511533013
# Question 1

full_name = "Annafi Al Ghifari"
nim = "2511533013"

# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
clean = full_name.strip().lower()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name + nim[-3:]
print(username)
