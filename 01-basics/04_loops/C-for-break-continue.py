# for-in-range break & continue
for y in range(1, 20):
   if y == 15:
      break
   elif y % 2 == 0:
      continue
   print(y, end = " ")
print()