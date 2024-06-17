# Write a function called find_greater_than() that takes two parameters: a list of numbers and an integer threshold.
# The function should create a new list containing all numbers in the input list greater than the given threshold.
# The order of numbers in the result list should be the same as in the input list. For example:
# >>> find_greater_than([-3, 2, 8, 15, 31, 5, 4, 8], 5)
# [8, 15, 31, 8]

def find_greater_than(numbers, threshold):
    greater_than = []

    for i in numbers:
        if i > threshold:
            greater_than.append(i)
    return greater_than


a = find_greater_than([-3, 2, 8, 15, 31, 5, 4, 8], 5)
print(a)
