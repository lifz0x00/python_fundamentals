# for (counted loop)

# for-in-range (start(0), finish(<5))
for i in range(5):
   print(f"{i}", end = " ")
print("")
print("---")

# for-in-range (start(0), finish(<10), step(+2))
for x in range(0, 10, 2):
   print(f"{x}", end = " ")
print("")
print("---")

# for-in list
companies = ["Facebook", "Apple", "Amazon", "Netflix", "Google"]
for company in companies:
   print(f"{company}", end = " ")
print()