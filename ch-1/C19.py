# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

if __name__ == '__main__':
    print([chr(a) for a in range(97, 123)])
