# R 1.5 Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.


def sum_List(n):
    return sum([a * a for a in range(n)])

if __name__=='__main__':
    print(sum_List(n))


sum_List(10)    
