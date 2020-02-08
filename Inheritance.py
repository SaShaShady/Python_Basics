'''6 types of inheritance
    1. single
    2.multiple
    3.multi level
    4.Heirarchical
    5.hybrid
    6.cycle'''

class parent:
    def __init__(self):
        print("Parent")
    def m1(self):
        print("Parent 2")
class child(parent):
    def __init__(self):
        print("Child")

a=child()
a.m1()

print("---------------------------------------------------------------")

class parent:
    def __init__(self):
        print("Parent")
    def m1(self):
        print("Parent 2")
class child(parent):
    def __init__(self):
        print("Child")
class child2(child):
    def m2(self):
        print("Child2")

a=child2()
a.m1()
a.m2()

print("---------------------------------------------------------------")


class parent:
    def __init__(self):
        print("Parent")
    def m1(self):
        print("Parent 2")
class child():
    def __init__(self):
        print("Child")
class child2(parent,child):
    def m2(self):
        print("Child2")

a=child2()
a.m1()

print("---------------------------------------------------------------")


class parent:
    def __init__(self):
        print("Parent")
    def m1(self):
        print("Parent 2")
class child(parent):
    def __init__(self):
        print("Child")
class child2(parent):
    def m2(self):
        print("Child2")
class grandchild(child,child2):
    def m3(self):
        print("grandchild")
a=grandchild()
a.m1()
a.m2()
a.m3()

print("---------------------------------------------------------------")


class parent:
    def __init__(self):
        print("Parent")
    def m1(self):
        print("Parent 2")
class child(parent):
    def __init__(self):
        print("Child")
class child2(parent):
    def m2(self):
        print("Child2")

a=child2()
a.m1()
a.m2()

print("---------------------------------------------------------------")

class p:pass
class q:pass
class p(q):pass
class q(p):pass

print("---------------------------------------------------------------")

'''multithreading
pdbc
deco
generator
types of func'''