'''
list: insert, update, delete
'''
print("*primary")
fruits = ["apple", "banana", "cherry", "durian"]
print(f"{fruits}")

# list update
print("---")
print("*update 'apple' -> 'mango'")
fruits[0] = "mango" # update index 0
print(f"{fruits}")

# list (append, insert)
print("---")
print("*append 'papaya'")
fruits.append("papaya") # insert value to last element
print(f"{fruits}")
print("*insert 'grape'")
fruits.insert(0, "grape") # insert value with index position
print(f"{fruits}")

# list delete with (pop, remove, del)
print("---")
print("*pop 'papaya'")
pop_last_element = fruits.pop() # remove last element
print(f"{fruits}")
print("*remove 'grape'")
fruits.remove('grape') # remove element with value
# fruits.remove(fruits[0]) # remove element with index position
print(f"{fruits}") 
print("*del 'durian'")
del fruits[3] # remove element with index position
print(f"{fruits}")