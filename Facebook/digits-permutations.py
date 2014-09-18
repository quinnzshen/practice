def permutation(digits):
    if len(digits) == 1:
        return map_digits(digits)
    else:
        answer = []
        for char in map_digits(digits[0]):
            x = permutation(digits[1:])
            for y in x:
                answer.append(char + y)
        return answer


def map_digits(digit):
    if digit == '1':
        return ['1']
    elif digit == '2':
        return ['2','a','b','c']
    elif digit == '3':
        return ['3', 'd', 'e', 'f']
    elif digit == '4':
        return ['4', 'g', 'h', 'i']
    elif digit == '5':
        return ['5', 'j', 'k', 'l']
    elif digit == '6':
        return ['6', 'm', 'n', 'o']
    elif digit == '7':
        return ['7', 'p', 'q', 'r', 's']
    elif digit == '8':
        return ['8', 't', 'u', 'v']
    elif digit == '9':
        return ['9', 'w', 'x', 'y', 'z']
    elif digit == '0':
        return ['0']


if __name__ == "__main__":
    print permutation('2')
    print permutation('22')
    print permutation('222')
    print permutation('1')
    print permutation('121')
