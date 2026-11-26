schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}
# 1.	6a (5 poin). Cetak hari dengan mata kuliah terbanyak dan jumlahnya, dengan format Busiest day: <day> (<count> courses).
busiest_day = ""
max_courses = -1

for day, courses in schedule.items():
    if len(courses) > max_courses:
        max_courses = len(courses)
        busiest_day = day

print(f"Busiest day: {busiest_day} ({max_courses} courses)")

# 2.	6b (5 poin). Minta input nama mata kuliah, lalu cetak jumlah hari mata kuliah itu muncul, dengan format <course>: <count> days.
target_course = input("Enter course name: ")
daycount = 0

for courses in schedule.values():
    if target_course in courses:
        daycount += 1

print(f"{target_course}: {daycount} days")