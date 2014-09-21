def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        return partial
    if s >= target:
        return None # if we reach the number why bother to continue

    for i in range(len(numbers)):
        potential_sums = []
        n = numbers[i]
        remaining = numbers[i+1:]
        answer = subset_sum(remaining, target, partial + [n])
        if answer:
            return answer

if __name__ == "__main__":
    a = subset_sum([3,9,4,5,7,10],15)
    print a
    #Outputs:
    #sum([3, 8, 4])=15
    #sum([3, 5, 7])=15
    #sum([8, 7])=15
    #sum([5, 10])=15quit()
