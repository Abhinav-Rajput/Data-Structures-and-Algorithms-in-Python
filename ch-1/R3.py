# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
#     one or more numbers, and returns the smallest and largest numbers, in the
#     form of a tuple of length two. Do not use the built-in functions min or
#     max in implementing your solution


def minMax(a):
    min = max = a[0]
    for i in a[1:]:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

if __name__ == '__main__':
    in_str = input("input numbers, separated")
    data = [float(d) for d in in_str.split()]
    data_minMAx = minMax(data)
    print("min :{} max: {}".format(data_minMAx[0],data_minMAx[1]))
