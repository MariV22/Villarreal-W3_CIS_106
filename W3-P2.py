def calculate_price_details(item, quantity):
  # Determine unit price based on item
  if item.upper() == 'A':
      unit_price = 10.00
  else:
      unit_price = 20.00

  # Compute extended price
  extended_price = quantity * unit_price

  # Display results
  print(f"Item: {item}")
  print(f"Unit Price: ${unit_price:.2f}")
  print(f"Extended Price: ${extended_price:.2f}")

# Get user input
item = input("Enter the item (A or B): ")
quantity = int(input("Enter the quantity of items: "))

# Calculate and display price details
calculate_price_details(item, quantity)
