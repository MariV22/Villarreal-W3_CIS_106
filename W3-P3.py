def calculate_order_details(number_of_books, cost_per_book):
  # Compute order total
  order_total = number_of_books * cost_per_book

  # Determine shipping charge
  if order_total > 50.00:
      shipping_charge = 0.00
  else:
      shipping_charge = 25.00

  # Display results
  print(f"Order Total: ${order_total:.2f}")
  print(f"Shipping Charge: ${shipping_charge:.2f}")

# Get user input
number_of_books = int(input("Enter the number of books to order: "))
cost_per_book = float(input("Enter the cost per book: "))

# Calculate and display order details
calculate_order_details(number_of_books, cost_per_book)
