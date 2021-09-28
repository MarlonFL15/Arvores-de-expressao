import operator
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
}

class tree(object):
    def __init__(self, values, start='', end=''):
        self.op = values[1] #+, -, *, /
        self.left = values[0]
        self.right = values[2]

        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.value}'

    def resolve(self):
        resultLeft = self.left.resolve() if type(self.left) == tree else self.left
        resultRight = self.right.resolve() if type(self.right) == tree else self.right

        return ops[self.op](float(resultLeft), float(resultRight))

