bill_total = 210  # Total bill amount

discount1 = 10    # Discount for bills >100 and <200
discount2 = 20    # Discount for bills >200

# Check the bill range
if bill_total > 100 and bill_total < 200:
    print("Bill is greater than 100!")  # Message for >100 and <200
    bill_total = bill_total - discount1 # Apply discount1
    
elif bill_total > 200:
    print("Bill is greater than 200!")  # Message for >200
    bill_total = bill_total - discount2 # Apply discount2
    
else:
    print("Bill is less than 100!")      # Message for <=100

# Print the final bill total
print("Total bill :" + str(bill_total))
