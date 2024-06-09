def calculate_price_details(quantity):
  # Determine unit price based on quantity
  if quantity >= 1000:
      unit_price = 3.00
  else:
      unit_price = 5.00

  # Compute extended price
  extended_price = quantity * unit_price

  # Compute tax (7% of extended price)
  tax = 0.07 * extended_price

  # Compute total (extended price + tax)
  total = extended_price + tax

  # Display results
  print(f"Quantity: {quantity}")
  print(f"Unit Price: ${unit_price:.2f}")
  print(f"Extended Price: ${extended_price:.2f}")
  print(f"Tax: ${tax:.2f}")
  print(f"Total: ${total:.2f}")

# Get user input
quantity = int(input("Enter the quantity of items: "))

# Calculate and display price details
calculate_price_details(quantity)