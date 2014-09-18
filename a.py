def solution(N):
    # write your code in Python 2.6
    max_bin_count = 0
    bin_count = 0
    begin = False
    while N != 0:
        if N & 1 == 1:
            begin = True
            max_bin_count = max(bin_count, max_bin_count)
            bin_count = 0
        elif N & 1 == 0 and begin is True:
            bin_count += 1
        N = N >> 1
    return max_bin_count

print solution(1041)
print bin(1041)

print solution(9)
print bin(9)

print solution(20)
print bin(20)

print solution(15)
print bin(15)