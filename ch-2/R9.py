# R-2.9 Implement the sub method for the Vector class of Section 2.3.3, so
# that the expression u−v returns a new vector instance representing the
# difference between two vectors.
# R-2.10 Implement the neg method for the Vector class of Section 2.3.3, so
# that the expression −v returns a new vector instance whose coordinates
# are all the negated values of the respective coordinates of v.


class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result


if __name__ == '__main__':
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v[4])
    u = v + v
    print(u)
    u = v - v
    print(u)
    total = 0
    for entry in v:
        total += entry
    x = Vector(3)
    x[0] = -100
    y = -x
    print(y)
    print(v)
    u = v + [5, 3, 10, 2, 1]
    print(u)
