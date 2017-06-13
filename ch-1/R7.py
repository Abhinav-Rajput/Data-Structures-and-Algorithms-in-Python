# R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying
# on Python’s comprehension syntax and the built-in sum function.


def squares_of_all_the_odd(k):
    assert k > 0
    return sum([x ** 2 for x in range(k) if x & 1])


if __name__ == '__main__':
    k = input("input num:")
    print('sum of squares_of_all_the_odd numbers less than {} is {}'.format(k, squares_of_all_the_odd(int(k))))
