class Node:
    def __init__(self, fun):
        self.fun = fun
        self.child = []
        self.f = -1
        self.g = -1


def f(v):
    if v.f >= 0:
        return v.f

    x = v.fun
    for kid in v.child:
        x += g(kid)

    y = g(v)

    v.f = max(x, y)
    return v.f


def g(v):
    if v.g >= 0:
        return v.g

    summ = 0
    for kid in v.child:
        summ += f(kid)

    v.g = summ
    return v.g


a = Node(10)

b = Node(5)
c = Node(16)

d = Node(4)
e = Node(2)

a.child.append(b)
a.child.append(c)

b.child.append(d)
b.child.append(e)

f(a)
print(a.f)
