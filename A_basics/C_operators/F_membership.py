# variable declarations
faang_companies = ["Facebook", "Apple", "Amazon", "Netflix", "Google"]

# expression
in_operator = "Facebook" in faang_companies
not_in_operator = "Microsoft" in faang_companies

# output
print(f'FAANG Companies: {faang_companies}')
print("---")
print(
  "Facebook in FAANG Companies?",
  in_operator
)
print(
  "Microsoft in FAANG Companies?",
  not_in_operator
)