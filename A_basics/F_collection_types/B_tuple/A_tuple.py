'''
tuple: ordered, unchangable
'''

# tuple (unchangable)
tuple_gender = ('Male', 'Female') # tuple initialization
tuple_empty = () # empty tuple

# access tuple value
print(f"Gender: {tuple_gender[0], tuple_gender[1]}") 
print(f"Empty : {tuple_empty}")

print()

# single tuple vs integer
tuple_single1 = (1,) # tuple
tuple_single2 = (1) # integer

print(f"Tuple Single 1: {type(tuple_single1)}")
print(f"Tuple Single 2: {type(tuple_single2)}")