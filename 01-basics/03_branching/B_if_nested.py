ticket = int(input("input ticket: "))
age = int(input("input age: "))

if ticket >= 1:
  if age >= 18:
    print("watch netflix")
  else:
    print("watch disney")
else:
  if ticket == 0:
    if age <= 13:
      print("watch youtube kids")
    elif age > 13:
      print("watch youtube")
  else:
    print("try again")