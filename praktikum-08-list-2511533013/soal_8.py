number_of_rows = 4
seats_per_row = 5

# Buat denah 4 baris x 5 kursi dengan list berbeda tiap baris
cinema = [["." for _ in range(seats_per_row)] for _ in range(number_of_rows)]

while True:
    for r in range(number_of_rows):
        print(f"Row {r + 1}: " + " ".join(cinema[r]) + " ")

    row_choice = int(input("Row (0 to stop): "))
    if row_choice == 0:
        break

    seat_choice = int(input("Seat: "))

    if 1 <= row_choice <= number_of_rows and 1 <= seat_choice <= seats_per_row:
        if cinema[row_choice - 1][seat_choice - 1] == "X":
            print("Seat already taken.")
        else:
            cinema[row_choice - 1][seat_choice - 1] = "X"
            print("Seat booked.")
    else:
        print("Invalid seat.")

seats_taken = 0
for row in cinema:
    for seat in row:
        if seat == "X":
            seats_taken += 1

print(f"Seats taken: {seats_taken}")