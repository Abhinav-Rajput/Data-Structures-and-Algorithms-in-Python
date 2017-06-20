class Empty(Exception):
    pass


class MyStack:
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity
        self._output = []
        self._precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self._topValue = -1

    def is_empty(self):
        return self._items == []

    def push(self, newItem):
        self._topValue += 1
        self._items.append(newItem)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        self._topValue -= 1
        return self._items.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._items[-1]

    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        try:
            a = self._precedence[i]
            b = self._precedence[self.top()]
            return True if a <= b else False
        except KeyError:
            return False

    def __len__(self):
        return len(self._items)

    def infixToPostFix(self, infixExpression):
        for i in infixExpression:
            if self.isOperand(i):
                self._output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while ((not self.is_empty()) and self.top() != '('):
                    a = self.pop()
                    self._output.append(a)
                if (not self.is_empty() and self.top() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while not self.is_empty() and self.notGreater(i):
                    self._output.append(self.pop())
                self.push(i)

        while not self.is_empty():
            self._output.append(self.pop())

        print("".join(self._output))


if __name__ == "__main__":
    inFixexp = "a+b*(c^d-e)^(f+g*h)-i"
    obj = MyStack(len(inFixexp))
    obj.infixToPostFix(inFixexp)
