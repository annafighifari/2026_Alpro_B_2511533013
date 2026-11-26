all_students = input().split()
submitted_list = input().split()

submitted_set = set(submitted_list)
not_submitted_set = set(all_students) - submitted_set

print(f"Submitted: {len(submitted_set)} students")
print(f"Not submitted: {len(not_submitted_set)} students")

for student in all_students:
    if student not in submitted_set:
        print(student)