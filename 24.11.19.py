'''polymorphism
overloading and overriding
overloading consists of const overloading and method and same w overriding
const overloading and method overloading not possible in python
OVERLOADING NOT POSSIBLE BS IF SAME NAME OF METHOD IT CONSIDERS LAST ONE
OVERRIDING ONLY POSSIBLE THROUGH INHERITANCE

class pi:
    def __init__(self):
        print("Const call")
    def __init__(self):
        print("Const call2")

    def disp(self):
        print("m2")
class ch(pi):
    def __init__(self):
        print("ch const")
        super().disp()
    def disp(self):
        print("m1")

c=ch()
c.disp()
b=pi()
b.disp()


print("*******************************************************************************")

class p:
    def property(self):
        print("land+cash+power+gold")
    def marry(self):
        print("Disha")

class m(p):
    def property(self):
        print("m method")
    def marry(self):
        print("doshi")

class c(m):

        def marry(self):
            print("katreena")
            super().marry()
s=c()
s.property()
s.marry()

    MRO METHOD
    Method resolution order


class p:
    def __init__(self):
        print("parent cons")
    def disp(self):
        print("parent method")
class c(p):
    def disp(self):
        print("child method")

print(c.mro())

s=c()
s.disp()

print("*************************************************************************")

class a:pass
class b(a):pass
class c(a):pass
class d(b,c):pass

print(a.mro())
print(b.mro())
print(c.mro())
print(d.mro())

print("***************************************************************************")'''

class a:pass
class b(a):pass
class c(a):pass
class d(a):pass
class e(b,c):pass
class f(c,d):pass
class p(e,f,d):pass


print(a.mro())
print(b.mro())
print(c.mro())
print(d.mro())
print(e.mro())
print(f.mro())
print(p.mro())


'''
IT USES DFS ALGORITHM
C3 ALGORITHM:
P= p+e+f+d
=p+(ebcao+fcdao+dao)
=p+e




1.SO BASICALLY FIRST DO MRO OF ALL ITS PARENTS
2.THEN DO MRO OF ALL PARENTS
3.THEN TAKE FIRST STRING EBCAO IN ABV EG
4.THEN TAKE FIRST ELEMENT OF STRING
5.IF NOT THERE IN ANY OTHER STRING THEN POP IT OUT
6.IF THERE IN ANY OTHER STRING THEN MOVE TO NEXT STRING THEN POP IT AND THEN CONTINUE FROM NEW STRING
7.THIS ALGO DOESNT GO TO BACK ELEMENT IT ONLY GOES IN FRONT
CAO,FCDAO,DAO
NOW F POPS OUT
THEN CAO,CDAO,DAO
ELIINATE C NOW
HENCE AO,DAO,DAO
NOW CONSIDER DAO
IT MOVES TO SECOND DAO
D POPS OUT
AO,AO,AO
NOW A POPS OUT
THEN O POPS OUT
'''