# Create two functions: print_five_times() and speak(). The function print_five_times() should accept one parameter (
# called sentence) and print it five times. The function speak(sentence, repeat) should have two parameters: sentence
# (a string of letters), and repeat (a Boolean with a default value set to False). If the repeat parameter is set to
# False, the function should just print a sentence once. If the repeat parameter is set to True, the function should
# call the print_five_times() function.

def print_five_time(sentence):
    for print_five_time in range(5):
        print(sentence)


def speak(sentence, repeat=False):
    if repeat:
        print_five_time(sentence)
    else:
        print(sentence)


print(speak("hello world,True"))
print(speak("hello world,False"))
