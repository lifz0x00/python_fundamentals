int_num = 77
print(f'int num type  : {type(int_num)}')
float_num = 3.14
print(f'float num type: {type(float_num)}')
new_num = int_num + float_num # implicit_conversion -> automatically 
print(f'new num type  : {type(new_num)}')

print('---')

str_num = "88"
int2_num = 17
str_num = int(str_num) # explicit_conversion -> v = T(v)
sum_str_int = str_num + int2_num
print(f'sum: {sum_str_int}')
print(f'str_num type: {type(str_num)}')