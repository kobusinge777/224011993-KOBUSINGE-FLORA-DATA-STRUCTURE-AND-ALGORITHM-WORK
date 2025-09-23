import array

# ---- Integers ----
vaccination_counts = [120, 85, 90, 150, 60, 110, 95]

total = sum(vaccination_counts)
average = total / len(vaccination_counts)
minimum = min(vaccination_counts)
maximum = max(vaccination_counts)

print("Total:", total)
print("Average:", average)
print("Min:", minimum)
print("Max:", maximum)

# ---- Strings ----
report = (
    f"Vaccination Queue Report:\n"
    f"Total vaccinations = {total}\n"
    f"Average per center = {average:.2f}"
)
summary = f"Highest = {maximum}, Lowest = {minimum}"
print(report)
print(summary)

# ---- Booleans ----
threshold = 100
if average > threshold and maximum > 140:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# ---- Lists ----
queue_list = ["Center A", "Center B", "Center C", "Center D"]
print("Before:", queue_list)

# Add new element
queue_list.append("Center E")

# Remove one based on condition
if "Center C" in queue_list:
    queue_list.remove("Center C")

# Sort
queue_list.sort()
print("After:", queue_list)

# ---- Arrays ----
arr = array.array('i', vaccination_counts)
array_sum = sum(arr)
print("Sum using array:", array_sum)
print("Check with list sum:", total)

# ---- Dictionaries ----
records = [
    {"id": 1, "name": "Center A", "value": 120},
    {"id": 2, "name": "Center B", "value": 85},
    {"id": 3, "name": "Center C", "value": 90},
]

# Update one record
records[1]["value"] = 95  # update Center B

# Delete another record
records = [r for r in records if r["id"] != 3]

# Compute total value
dict_total = sum(r["value"] for r in records)

print("Updated Records:", records)
print("Total value across records:", dict_total)
