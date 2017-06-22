# Input : ab aa aa bcd ab
# Output : 3
# As aa, aa destroys each other so, ab bcd ab is the
# new sequence.

# Input :  tom jerry jerry tom
# Output : 0
# As first both jerry will destroy each other.
# Then sequence will be tom, tom they will also destroy
# each other. So, the final sequence doesn't contain any
# word.


class Empty(Exception):
    pass


class MyStack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, newItem):
        self._items.append(newItem)

    def pop(self):
        if self.is_empty():
            raise ('Stack is Empty')
        return self._items.pop()

    def top(self):
        if self.is_empty():
            raise ('Stack is Empty')
        return self._items[-1]

    def removeConsecutiveSame(self, v):
        st = []
        st = v.split()
        for i in st:
            if self.is_empty():
                self.push(i)
            elif self.top() == i:
                self.pop()
            else:
                self.push(i)
        print(self._items, end='')


def main():
    strr = 'ab aa aa bcd ab'
    m = MyStack()
    m.removeConsecutiveSame(strr)


if __name__ == '__main__':
    main()
