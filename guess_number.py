# Problem: Write a function which determines an unknown integer using another (given) function, check_guess(x), which returns -1 if x is too low, 0 if x is right, and 1 if x is too high.

# Feel free to adjust the check_guess interface, write unit tests, run your code, and use the REPL!

def check_guess(guess):
    HIDDEN_NUMBER = 112341234
    if guess < HIDDEN_NUMBER:
        # Too low!
        return -1 
    elif guess > HIDDEN_NUMBER:
        # Too high!
        return 1
    else:
        # Just right.
        return 0

def guess_number():
    initial_guess = 0
    upper_bound = float("inf")
    lower_bound = float("-inf")
    
    if check_guess(initial_guess) == 1:
        upper_bound = initial_guess
        lower_bound = -10
        while check_guess(lower_bound) == 1:
            upper_bound = lower_bound
            lower_bound *= 10
        return guess_number_bounded(lower_bound, upper_bound)    
        
    elif check_guess(initial_guess) == -1:
        lower_bound = initial_guess
        upper_bound = 10
        while check_guess(upper_bound) == -1:
            lower_bound = upper_bound
            upper_bound *= 10
        return guess_number_bounded(lower_bound, upper_bound)
    else:
        return initial_guess

def guess_number_bounded(lower_bound, upper_bound):
    found = False
    answer = 0
    while not found:
        guess = (upper_bound + lower_bound) / 2
        response = check_guess(guess)
        if response == 1:
            upper_bound = guess
        elif response == -1:
            lower_bound = guess
        else:
            answer = guess
            found = True
    return answer


