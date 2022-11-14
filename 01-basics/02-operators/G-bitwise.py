# variable declarations
bin_2 = 2
bin_64 = 64

# expression
bw_and = bin_2 & bin_64
bw_or = bin_2 | bin_64
bw_xor = bin_2 ^ bin_64
bw_not_bin_2 = ~bin_2
bw_not_bin_64 = ~bin_64
bw_right_shift = bin_2 >> bin_64
bw_left_shift = bin_64 << bin_2

# output
print(f"[and]") 
print(f"bin  {bin_2}: {bin_2:>08b}")
print(f"bin {bin_64}: {bin_64:>08b}")
print(f"binary: {bw_and:>08b} is {bw_and}")
print("---")
print(f"[or]") 
print(f"bin  {bin_2}: {bin_2:>08b}")
print(f"bin {bin_64}: {bin_64:>08b}")
print(f"binary: {bw_or:>08b} is {bw_or}")
print("---")
print(f"[xor]")  
print(f"bin  {bin_2}: {bin_2:>08b}")
print(f"bin {bin_64}: {bin_64:>08b}")
print(f"binary: {bw_xor:>08b} is {bw_xor}")
print("---")
print(f"[not]")
print(f"bin  {bin_2}: {bin_2:>08b}")
print(f"bin {bin_64}: {bin_64:>08b}")
print(f"binary: {bw_not_bin_2:>08b} is {bw_not_bin_2}")
print(f"binary: {bw_not_bin_64:>08b} is {bw_not_bin_64}")
print("---")
print(f"[right shift]")
print(f"bin  {bin_2}: {bin_2:>08b}")
print(f"bin {bin_64}: {bin_64:>08b}")
print(f"binary: {bw_right_shift:>08b} is {bw_right_shift}")
print("---")
print(f"[left shift]")
print(f"bin  {bin_2}: {bin_2:>08b}")
print(f"bin {bin_64}: {bin_64:>08b}")
print(f"binary: {bw_left_shift:>08b} is {bw_left_shift}")