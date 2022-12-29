# func() 1 return
def square_area(side):
  return side * side

# print(f'Square Area 10: {square_area(10)}') # call func()

# func() +1 return
def percentage(total, result):
  if (total >= 0 and total <= result): # 30 and true -> true
    return (total / result) * 10  # (30 / 60) * 10 -> 0.5 * 10 -> 5.0
  
  return False # false

print(percentage(30, 60))
