# Write a program that asks the user for a number then prints the following sentence that number of times:
# ‘I am back to check on my skills!’ If the number is greater than 10, print this sentence instead:
# ‘Python conditions and loops are a piece of cake.’ Assume you can only pass positive integers.

a = int(input("Enter the number"))
if a <= 10:
    print("I am back to check on my skills!")
else:
    print("Python conditions and loops are  a piece os cake.")
