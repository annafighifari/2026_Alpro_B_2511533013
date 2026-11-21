LAST_DIGIT = 3  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for day in range(1, 8):
    amount = int(input(f"Day {day}: "))
    expenses.append(amount)

total = 0
highest_amount = expenses[0]
highest_day = 1
days_above_limit = 0

for i in range(len(expenses)):
    total += expenses[i]
    if expenses[i] > highest_amount:
        highest_amount = expenses[i]
        highest_day = i + 1
    if expenses[i] > daily_limit:
        days_above_limit += 1

average = total / len(expenses)

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_amount})")
print(f"Days above limit: {days_above_limit}")