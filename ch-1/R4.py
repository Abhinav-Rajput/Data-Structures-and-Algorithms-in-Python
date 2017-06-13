# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.


def sum_of_squares(n):
    sum = 0
    for i in range(1, n):
        sum += i * i
    return sum

if __name__=='__main__':
    in_str = input("Input a number")    
    print("the sum of the squares of all the positive integers smaller than n",sum_of_squares(int(in_str)))
