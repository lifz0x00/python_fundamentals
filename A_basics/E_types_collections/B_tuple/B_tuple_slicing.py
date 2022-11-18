'''
slicing = a technique for cutting values in a tuple
index     = 0, 1, 2, 3
elements  = 1, 2, 3, 4
negative  = elements - index
'''

# tuple (unchangeable)
fruits = ("apple", "banana", "cherry", "durian")
print(f"fruits: {fruits}")

# tuple slicing (start:end)
print("---")
print("start-end")
print(f"[0:2] is {fruits[0:2]}") # start(0) -> end(2) -> print(0,1)
print(f"[0:-1] is {fruits[0:-1]}") # start(0) -> end(4-1=3)) -> print(0,1,2)
print(f"[-4:-2] is {fruits[-4:-2]}") # start(4-4=0) -> end(4-2=2) -> print(0,1)
print(f"[-1:3] is {fruits[-1:3]}") # start(4-1=3) -> end(3) -> print()
print(f"[0:] is {fruits[0:]}") # start(0) -> end -> print(0,1,2,3)
print(f"[:2] is {fruits[:2]}") # start(0) -> end(2) -> print(0,1)

# tuple slicing (start:end:step)
print("---")
print("start-end-step")
print(f"[0:4:2] is {fruits[0:4:2]}") # start(0) -> end(4) -> step(2) -> print(0,2)