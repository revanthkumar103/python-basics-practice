print("Welcome to Marks Average Calculator")

# Input marks
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculate total and average
total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5

# Display result
print("\n----- Result -----")
print("Total Marks:", total)
print("Average Marks:", average)
