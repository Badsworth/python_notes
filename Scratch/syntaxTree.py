# Trees: https://www.youtube.com/watch?v=7tCNu4CnjVc

class Expr:
    pass


class Times(Expr):
    def __init__(self, l, r)
        self.l = l
        self.r = r


class Plus(Expr):
    def __init__(self, l, r)
        self.l = l
        self.r = r


class Const(Expr):
    def __init__(self, val)
        self.val = val


class Var(Expr):
    def __init__(self, name)
        self.name = name


e1 = Times((Const(3), Plus(Var("y"), Var("x")))

e2=Plus(Times(Const(3), Var("y")), Var("x"))
