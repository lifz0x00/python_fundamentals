# set
set_alphabet = {'A', 'B', 'C', 'D', 'E'}
print(f"set       : {set_alphabet}")

# set insert one-by-one (add) & insert more than one (update) 
set_alphabet.add('F') 
set_alphabet.add('G')
print(f"set_add   : {set_alphabet}")
set_alphabet.update('H', 'I', 'J')
print(f"set_update: {set_alphabet}")

print("---")

# set delete
my_set = {'LIFZ' , 'PANJI', 77, 3.14 , ('A', 'B'), False, True}
print(f"my_set          : {my_set}")
my_set.remove(3.14) # delete one item, error when 3.14 not in the set
print(f"my_set_remove   : {my_set}")
my_set.discard(('A', 'B'))
print(f"my_set_discard  : {my_set}") # delete item, error when 'A', 'B' not in the set
my_set_pop = my_set.pop() # remove item on the left side 
print(f"my_set_pop      : {my_set_pop}") # show deleted value
print(f"my_set_after_pop: {my_set}")
my_set.clear()
print(f"my_set_clear    : {my_set}")