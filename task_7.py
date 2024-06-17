# 7. As you see, we've prepared the test_results variable for you. Your task is to iterate over the values of the
# dictionary and print all names of people who received less than 45 points.
# test_results = {'Jenny': 50, 'Mathew': 45, 'Joe': 30, 'Peter': 40, 'Agness': 50, 'Samantha': 45, 'John': 20}
test_results = {'Jenny': 50, 'Mathew': 45, 'Joe': 30, 'Peter': 40, 'Agness': 50, 'Samantha': 45, 'John': 20}
for name, points in test_results.items():
    if points < 45:
        print(name)
