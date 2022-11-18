def factorial(n):
  if n == 0: # base_case
    return 1

  return n * factorial(n-1) # recursive_call

n = 5
print(f"!{n}: {factorial(n)}")

'''
factorial(5)
if 5 == 0 -> False -> 5 * factorial(5-1) -> 5 * factorial(4)
if 4 == 0 -> False -> 4 * factorial(4-1) -> 5 * (4 * factorial(3))
if 3 == 0 -> False -> 3 * factorial(3-1) -> 5 * (4 (3 * factorial(2)))
if 2 == 0 -> False -> 2 * factorial(2-1) -> 5 * (4 *  (3 * (2 * factorial(1)))
if 1 == 0 -> False -> 1 * factorial(1-1) -> 0 -> 5 * (4 *  (3 * (2 * 1)))

5 * (4 * (3 * (2 * 1))
5 * (4 * (3 * 2))
5 * (4 * 6)
5 * 24
'''