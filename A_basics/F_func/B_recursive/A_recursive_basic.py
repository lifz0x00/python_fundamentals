def show(n):
  if n == 0: # base_case
    return False

  print(f"n: {n}")
  return show(n-1) # recursive_call

show(3)

'''
show(3) -> print(3)
return show(3-1) -> print(2)
return show(2-1) -> print(1)
return show(1-1) -> 0 -> STOP
'''