# Initializing the variables

store_name = input("What is the name of the store:")
location = input("Where is the store located:")
rating = float(input("What is the rating of the shop out of 5.0:"))
is_open = True
employee_count = int(input("How many employees work there:"))

# Printing the values

print(f"The stores name is:{store_name}")
print(f"The store is located at:{location}")
print(f"The stored is rated as:{rating}")
print(f"Is the store open: {is_open}")
print(f"The number of people employeed there are: {employee_count}")

# Types of the variables

print(f"The type of the variable store_name is: {type(store_name)}")
print(f"The type of the variable rating is : {type(rating)}")
print(f"The type of variable is_open is: {type(is_open)}")
print(f"The type of variable employee_count is: {type(employee_count)}")

# Basic Arithmetic

revenue_q1 = float(input("What was the revenue in 1st quater: "))
revenue_q2 = float(input("What was the revenue in the second quater: "))

total_revenue = revenue_q1 + revenue_q2
avg_revenue = total_revenue / 2
print(f"The total revenue is :${total_revenue:,.2f}")
print(f"The average revenue is: ${avg_revenue:,.2f}")
