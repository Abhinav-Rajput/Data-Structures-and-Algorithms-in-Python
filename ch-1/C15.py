# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def is_Distnict(s):
    a = s[0]
    n = len(s)
    for i in range(1, n):
        if a == s[i]:
            return False
        a = s[i]
    return True


if __name__ == '__main__':
    s = input('input integers, separated by blank')
    s = [int(a) for a in s.split()]
    print("if the sequence is distinct", is_Distnict(s))
