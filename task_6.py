# Create a function find_short_long_word(words_list). The function should return a tuple of the shortest word in the
# list and the longest word in the list (in that order). If there are multiple words that qualify as the shortest
# word, return the first shortest word in the list. And if there are multiple words that qualify as the longest word,
# return the last longest word in the list. For example, for the following list:
#
# words = ['go', 'run', 'play', 'see', 'my', 'stay']
# the function should return
#
# ('go', 'stay')
def find_short_long_word(words_list):
    shortest = words_list[0]
    longest = words_list[0]
    for i in words_list:
        if len(i) < len(shortest):
            shortest = i
        elif len(i) > len(longest):
            longest = i
    return shortest, longest


a, b = find_short_long_word(['go', 'run', 'play', 'see', 'my', 'stay'])
print(a, b)
