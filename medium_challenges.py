def trailing_factorial(a):
    """Write an algorithm which computes the numbers of trailing zeros in n factorial.

    Based on math, the amount of trailing zeros is determined by how many pairs of 2's & 5's we can find. 
    Since there will always be more 2's than 5's, we can just count the amount of 5's present in the factorial.

    >>> trailing_factorial(5)
    1
    >>> trailing_factorial(19)
    3
    """
    answer = 0
    for x in xrange(1, a + 1):
        if x % 5 == 0:
            answer += number_of_fives(x)
    return answer

def number_of_fives(x):
    """Helper function for trailing factorials."""
    answer = 0
    while x >= 5:
        x = x / 5
        answer += 1
    return answer

def master_mind(solution, guess):
    """Given a guess and a solution, 
    return the number of hits and psuedo-hits.

    >>> master_mind("RGBY", "GGRR")
    (1, 1)
    >>> master_mind("RGGB", "YRGB")
    (2, 1)
    """
    hits = 0
    psuedo_hits = 0
    missed_solution = dict()
    missed_guess = dict()

    for index in xrange(4):
        if solution[index] == guess[index]:
            hits += 1
        else:
            if solution[index] in missed_solution.keys():
                missed_solution[solution[index]] += 1
            else:
                missed_solution[solution[index]] = 1
            if guess[index] in missed_guess.keys():
                missed_guess[guess[index]] += 1
            else:
                missed_guess[guess[index]] = 1
    for char, count in missed_solution.items():
        if char in missed_guess.keys():
            psuedo_hits += min(missed_guess[char], count)

    return (hits, psuedo_hits)

def min_sorted(int_array):
    """
    >>> min_sorted([1,2,3,6,7,4,5,9])
    (3, 6)
    >>> min_sorted([1,8,10,9,10,14])
    (2, 3)
    """
    left_index = 0
    right_index = 0
    for index in xrange(1, len(int_array)):
        if int_array[index] < int_array[index - 1]:
            left_index = index - 1 
            break
    for index in range(0, len(int_array) - 1)[::-1]:
        if int_array[index] < int_array[index - 1]:  
            right_index = index
            break
    sorted_beginning = int_array[0:left_index]
    sorted_middle = int_array[left_index:(right_index + 1)]
    sorted_end = int_array[(right_index + 1):len(int_array)]
    # print sorted_beginning, sorted_middle, sorted_end, left_index, right_index
    unsorted_min = min(sorted_middle)
    unsorted_max = max(sorted_middle)
    # print unsorted_max, unsorted_min
    for index in xrange(len(sorted_beginning)):
        if int_array[index] > unsorted_min:
            left_index = index
            break
    for index in range(right_index, len(int_array))[::-1]:
        if int_array[index] < unsorted_max:
            right_index = index
            break
    return (left_index, right_index)

def largest_contiguous_sum(int_array):
    """ Given an array of integers, find the contiguous sequence
        with the largest sum

    >>> largest_contiguous_sum([2,3,-8,-1,2,4,-2,3])
    7
    """
    if not int_array:
        return float("-inf")
    else:
        largest_sum = 0
        current_sum = 0
        for index in xrange(len(int_array)):
            current_sum += int_array[index]
            if largest_sum < current_sum:
                largest_sum = current_sum
            elif current_sum < 0: 
                current_sum = 0        
        return largest_sum

def rand7():
    def rand5():
        import random
        return random.randint(0,4)
    while True:
        random = (rand5(), rand5())
        if random == (0, 0) or random == (0, 1) or random == (0, 2):
            return 0
        elif random == (0, 3) or random == (0, 4) or random == (1, 0):
            return 1
        elif random == (1, 1) or random == (1, 2) or random == (1, 3):
            return 2
        elif random == (1, 4) or random == (2, 0) or random == (2, 1):
            return 3
        elif random == (2, 2) or random == (2, 3) or random == (2, 4):
            return 4
        elif random == (3, 0) or random == (3, 1) or random == (3, 2):
            return 5
        elif random == (3, 3) or random == (3, 4) or random == (4, 0):
            return 6

def rand7_test():
    sample_size = 1000000
    random_results = {k: 0 for k in xrange(7)}
    for _ in xrange(sample_size):
        random_results[rand7()] += 1
    return random_results

if __name__ == "__main__":
    import doctest
    doctest.testmod()
