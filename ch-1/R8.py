# R1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index
# −n≤k<0, what is the equivalent index j ≥0 such that s[j] references
# the same element?

# it will be i ~ -(len(s)-i), where i in range(len(s))


def negativeIntegers(s):
    for i in range(0, len(s)):
        print(s[i], i, s[-(len(s) - i)], -(len(s) - i))


negativeIntegers('abcdefgh')
