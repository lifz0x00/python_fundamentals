'''
dictionary: unordered, changeable, unique(key), key & value
'''
# dict initialization
factfulness = {
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

print(f"book: {factfulness}")
print("---")

# access dict
print(f"Book         : {factfulness['title']}")
print(f"Category     : {factfulness['category'][0]}")
print(f"Published Day: {factfulness['published']['day']}")