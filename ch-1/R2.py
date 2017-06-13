# R - 1.2 Write a short Python function, is even(k), that takes an integer value and
#     returns True if k is even, and False otherwise. However, your function
#     cannot use the multiplication, modulo, or division operators.


def is_Even(n):
    return not n & 1

if __name__=='main':
    n = input("input an int")
    print("is even ? ",is_Even(int(n)))    

    
