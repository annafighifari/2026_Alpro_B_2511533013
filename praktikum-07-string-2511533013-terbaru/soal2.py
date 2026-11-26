# Name: Annafi Al Ghifari
# NIM: 2511533013
# Question 1

text = "  belajar python di kampus  "
clean = text.strip()
print(len(text), len(clean))
print(clean.find("python"))
print(clean.find("java"))
print(clean.count("a"))
print(clean.replace("kampus", "rumah"))
print(clean.title())
print("py" in clean)
print("Py" in clean)
