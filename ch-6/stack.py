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
            raise Empty('Stack is Empty')
        return self._items.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._items[-1]

    def __len__(self):
        return len(self._items)

if __name__=="__main__":
    s = MyStack()
    # s.pop()
    s.push(5)
    s.push(3)
    print(len(s))
    print(s.pop())
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())
    s.push(7)
    s.push(9)
    print(s.top())
    s.push(4)
    print(len(s))
    print(s.pop())
    s.push(6)
    


