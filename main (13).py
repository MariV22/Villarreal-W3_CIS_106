def calculate_warranty_details(name, cost):
  # Determine warranty cost based on cost of appliance
  if cost > 1000:
      warranty_cost = 0.10 * cost
  else:
      warranty_cost = 0.05 * cost

  # Compute total cost
  total_cost = cost + warranty_cost

  # Display results
  print(f"Appliance Name: {name}")
  print(f"Cost of Appliance: ${cost:.2f}")
  print(f"Cost of Warranty: ${warranty_cost:.2f}")
  print(f"Total Cost (Appliance + Warranty): ${total_cost:.2f}")

# Get user input
appliance_name = input("Enter the name of the appliance: ")
appliance_cost = float(input("Enter the cost of the appliance: "))

# Calculate and display warranty details
calculate_warranty_details(appliance_name, appliance_cost)