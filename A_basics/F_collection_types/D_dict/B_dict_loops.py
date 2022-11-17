# book
book1 = {
  "title": "Factfulness",
  "description": "Ten Reasons We're Wrong About the World",
  "category": [
    "Social Science", "Non-Fiction" 
  ],
  "published": {
    "day": 28,
    "month": "February",
    "year": 2018
  }
}

# OK
# print(book1)
# for key in book1:
  # print(f"{key}") # show keys directly default
  # print(f"{key}: {book1[key]}") # show keys & values default

# NOK
# print(book1.items())
# for key, item in book1.items():
  # print(f"{key}: {item}") # show keys & values with .items()

# OK
# print(book1.keys())
# for key in book1.keys():
  # print(f"{key}") # show keys directly with .keys()
  # print(f"{key}: {book1[key]}") # show keys & values with .keys()

# NOK
# print(book1.values())
# for value in book1.values():
  # print(f"{value}") # show values directyl with .values()