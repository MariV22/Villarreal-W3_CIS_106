def calculate_tax_details(last_name, dependents, gross_income):
  # Compute adjusted gross income
  adjusted_gross_income = gross_income - (dependents * 12000)

  # Determine tax rate based on adjusted gross income
  if adjusted_gross_income > 50000:
      tax_rate = 0.20
  else:
      tax_rate = 0.10

    # Compute income tax
  income_tax = adjusted_gross_income * tax_rate

  # If income tax is less than 0, set it to $100
  if income_tax < 0:
      income_tax = 100.00

  # Display results
  print(f"Last Name: {last_name}")
  print(f"Gross Income: ${gross_income:.2f}")
  print(f"Number of Dependents: {dependents}")
  print(f"Adjusted Gross Income: ${adjusted_gross_income:.2f}")
  print(f"Income Tax: ${income_tax:.2f}")

# Get user input
last_name = input("Enter your last name: ")
dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter your gross income: "))

# Calculate and display tax details
calculate_tax_details(last_name, dependents, gross_income)