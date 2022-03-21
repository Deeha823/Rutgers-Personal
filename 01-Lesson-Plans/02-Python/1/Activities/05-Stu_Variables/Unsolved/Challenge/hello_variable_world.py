# Percent Increase Bonus Activity

# Formulas
# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create float variable for original_price
org_price = 197.87

# Create float variable for current_price
current_price = 254.32

# Calculate difference between current_price and original_price
increase =  current_price - org_price

# Calculate percent_increase
percent_increase = increase / org_price * 100

# Print original_price
print(f"Apple's original stock price was ${org_price}")

# Print current_price
print(f"Apples current stock price is ${current_price}")

# Print percent_increase to 2 decimal places using string formatting
print(f"Apples percentage increase is % {round(percent_increase,2)}")