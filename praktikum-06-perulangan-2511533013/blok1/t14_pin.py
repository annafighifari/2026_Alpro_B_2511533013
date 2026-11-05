correct_pin = "1234"
MAX_ATTEMPTS = 3
attempt = 1

pin = input("Enter PIN: ")

while pin != correct_pin and attempt < MAX_ATTEMPTS:
    print("Incorrect PIN.")
    pin = input("Enter PIN: ")
    attempt += 1

if pin == correct_pin:
    print("Access granted")
else:
    print("Account locked")