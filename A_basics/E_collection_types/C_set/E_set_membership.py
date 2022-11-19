# set A and B
set_A = {'Alex', 'Bob', 'Charlie', 'Duke'}
set_B = {'Bob', 'Duke', 'Eric', 'Fanny'}
print(f'A: {set_A}')
print(f'B: {set_B}')
print("---")

# union (gabungan) A | B -> delete duplicate_value(AB) and combine_set(AB) 
union_set = set_A | set_B
print(f"Union               : {union_set}")

# intersection (irisan) A & B -> delete unduplicate_value(AB) and show duplicate_set(AB)
intersection_set = set_A & set_B
print(f"Intersection        : {intersection_set}")

# difference(selisih) A - B -> delete duplicate_value(AB) and show set(A)
difference_set = set_A - set_B
print(f"Difference          : {difference_set} ")

# symmetric_difference() A ^ B ->  delete duplicate_value(AB) and show set(AB)
symmetric_difference = set_A ^ set_B
print(f"Symmetric Difference: {symmetric_difference}")