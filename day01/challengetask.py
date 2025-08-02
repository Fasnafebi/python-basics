grades = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78
}

print("Grade Tracker Students:", grades)

average = sum(grades.values()) / len(grades)
print(f"Average grade: {average:.1f}")

highest = max(grades, key=grades.get)
lowest = min(grades, key=grades.get)
print(f"Highest scorer: {highest} ({grades[highest]})")
print(f"Lowest scorer: {lowest} ({grades[lowest]})")

grades['Diana'] = 88
print("\nAfter adding Diana:", grades)

grades['Alice'] = 90
print("After updating Alice's grade:", grades)

average = sum(grades.values()) / len(grades)
highest = max(grades, key=grades.get)
lowest = min(grades, key=grades.get)

print(f"\nUpdated average grade: {average:.1f}")
print(f"Highest scorer: {highest} ({grades[highest]})")
print(f"Lowest scorer: {lowest} ({grades[lowest]})")