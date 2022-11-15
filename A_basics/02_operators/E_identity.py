# variable declarations
x = 10
y = 10
list_A = [1, 2, 3, 4, 5]
list_B = [1, 2, 3, 4 ,5]

# expression
is_identity = x is y
is_not_identity = list_A is not list_B

# output & check memory location
print(f"x: {x}")
print(f"y: {y}")
print(f"list_A: {list_A}")
print(f"list_B: {list_B}")
print("---")

print(f"{x} is {y}: {is_identity}") # same value + same memory
print(f"id {x}: {id(x)}") # id -> check memory location 
print(f"id {y}: {id(y)}") # id -> check memory location 
print("---")

print(f"{list_A} is not {list_B}: {is_not_identity}") # same value + different memory
print(f"id {list_A}: {id(list_A)}") # id -> check memory location 
print(f"id {list_B}: {id(list_B)}") # id -> check memory location 
