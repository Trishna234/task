# 2. Below is a string, text. It contains a long string of characters. Your task is to iterate over the characters of
# the string, count uppercase letters and lowercase letters, and print the result: Use the string.islower() and
# string.isupper() methods to check if a string contains lowercase and uppercase characters. text =
# "ABgvddVICJSdkeprsmgnUTPDvndhtuwPOTNRSjfisuRNSUesajdsa"
from itertools import count

text = "ABgvddVICJSdkeprsmgnUTPDvndhtuwPOTNRSjfisuRNSUesajdsa"
uppercase = 0
lowercase = 0
for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
print(f"uppercase letter:{uppercase}")
print(f"uppercase letter:{lowercase}")





