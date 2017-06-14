# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

if __name__ == '__main__':
    print([(a + (a**2)) for a in range(10)])
