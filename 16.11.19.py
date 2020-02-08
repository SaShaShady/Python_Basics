'''3 types of variables in python
1 instance variable
2. static variable
3. local variable
 Q.Where can we declare instance  variable?
 Ans : inside cons by using self variable
     : inside instance method using self
     : outside of class using  reference variable

class student:
    def __init__(self,age,name):
        self.name=name
        self.age=age
    def disp(self):
        self.gender=gender
        print("My name is {}.I am {} years old.".format(self.name,self.age))


c=student(20,"Sakshi")
'c.gender="male"
c.disp()



class student:
    def __init__(self):
        self.a=20
        self.b=30
    def disp(self):

        print(self.a)
        print(self.b)


c=student()
print(c.a,c.b)
c.disp()
accessed inside class and outside class through obj 

STATIC VARIABLE
Where to declare:
inside cons using class name of self variable
inside inst method by class name or self
inside class method by using cls or class name
outside of class by using class name
inside static method by using class name or cls


class student:
    def __init__(self):
        self.a=20
        student.y=880

    def disp(self):

        student.b=30
        self.c=40

    @classmethod
    def display(cls):
        cls.d=60
        student.e=70

    @staticmethod
    def static():
        student.z=100

print(student.__dict__)
c=student()
c.disp()
c.display()
c.static()
print(c.a,c.b,c.c,c.d,c.e,c.z,c.y)

print("-----------------------------------------------------------------------------")

class student:
    a=10
    def __init__(self):
        print(self.a)
        print(student.a)

    def disp(self):

        print(student.a)
        print(self.a)

    @classmethod
    def display(cls):
        print(cls.a)
        print(student.a)

    @staticmethod
    def static():
        print(student.a)

print(student.__dict__)
c=student()
c.disp()
c.display()
c.static()


LOCAL VARIABLE
inst -obj level
static- class level
local-method level

class student:
    def __init__(self):
        a=10
        print(a)
    def disp(self):
        b=20
        print(b)
c=student()
c.disp()

INSTANCE METHOD
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def disp(self):
        print("My name is {}.I have {} marks.".format(self.name,self.marks))
    def grade(self):
        if self.marks>=70:
            print("First class")
        elif self.marks >= 50:
            print("Second class")
        elif self.marks >= 30:
            print("Pass")
        else :
            print("Fail")

n=int(input("Enter total number of students"))
for i in range(n):
    name = input("Enter name")
    marks = int(input("Enter marks"))
    c=student(name,marks)
    c.disp()
    c.grade()

class animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} walks with {} legs".format(name,cls.legs))
s=animal()
s.walk("Dog")
s.walk("Cat")

class math:
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def sub(x,y):
        return x-y
s=math()
print(s.add(10,20))
print(s.sub(30,40))'''

class outer:
    def __init__(self):
        print("outer")
    class inner:
        def __init__(self):
            print("Inner")

        @staticmethod
        def disp():
            print("Inner method")


c=outer()
d=c.inner()
d.disp()
print("++++++++++++++++++++______________++++++++++++++++++++++")
outer().inner().disp()
