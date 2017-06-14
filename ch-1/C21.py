# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).
if __name__ == '__main__':
    s = []
    print('Input anything end it with ctrl-z')
    try:
        while True:
            a = input()
            s.append(a)
    except EOFError:
        s.reverse()
        print('the reversed inputs are')
        for i in s:
            print(i)
