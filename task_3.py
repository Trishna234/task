# Create a function named is_triangle_possible() that accepts three positive numbers. It should return True if it is
# possible to create a triangle from line segments of given lengths and False otherwise. With 3 numbers,
# it is sometimes, but not always, possible to create a triangle: You cannot create a triangle from a = 13, b = 2,
# and c = 3, but you can from a = 13, b = 9, and c = 10.
def is_triangle_possibl(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


print(is_triangle_possibl(13, 2, 3))
print(is_triangle_possibl(13, 9, 10))
