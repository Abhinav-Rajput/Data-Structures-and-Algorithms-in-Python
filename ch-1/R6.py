# R1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def squares_of_all_the_odd(n):
    return sum([x*x for x in range(n) if x%2!=0])

if __name__=='__main__':
    print(squares_of_all_the_odd(8))    