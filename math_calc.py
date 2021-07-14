def calc_string(arg):
    calc_object = calc(int(arg[0]), arg[1], int(arg[2]))
    result = [
        calc_object.add(),
        calc_object.sub(),
        calc_object.prod(),
        calc_object.div(),
    ]
    for i in result:
        if i is not None:
            return i


class calc:
    def __init__(self, a, oper, b):
        self.a = a
        self.b = b
        self.oper = oper

    def add(self):
        if self.oper == "+":
            return self.a + self.b

    def sub(self):
        if self.oper == "-":
            return self.a - self.b

    def prod(self):
        if self.oper == "*":
            return self.a * self.b

    def div(self):
        if self.oper == "/":
            return self.a / self.b
