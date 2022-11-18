city, province = "Bandung", 'Jawa Barat' # global variable

def city_province():
  city = "Jakarta Barat"
  province = "DKI Jakarta" # local variable
  print(f"{city}, {province}")

print('Call city_province()')
city_province() # print func() local

print('---')

print('Direct print()')
print(f"{city}, {province}") # print global variable