'''f=int(input("Enter"))
for i in range(-f,-1):

    for j in range(-1,-(i+1)):
        print('*',end=' ')
        print()'''

i=0
while i<10:
    i=i+1
    if i==7:
        continue
    print(i)


f='sakshi'


try:
    print(10/0)
except ZeroDivisionError:
    pass

a='Python is easy'
print(a.split())
print(len(a))
print(a.count('s'))
print(a)
print(a.strip())
print(a.rstrip())
print(a.lstrip())
b=a.split()
print(''.join(b))
print('_'.join(b))
print(a.replace('Python','java'))
b=a.replace('Python','java')
print(id(a))
print(id(b))
'String is immutable but when used replace it basically stores the replaced one in a new obj and then' \
'prints the new one therefore total 2 strings now'
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a[::-1])

c=input('Enter string\n')
length=len(c)-1
output=''
while length>=0:
    output=output+c[length]
    length=length-1
print(output)

'''star pattern in row col form
for row in range(4):
    for col in range(4):
        if row==0 and col==0:
            print('*',end=' ')
        elif row==1 and col in {0,1}:
            print('*',end=' ')
        elif row==2 and col in {0,1,2}:
            print('*',end=' ')
        elif row==3 and col in {0,1,2,3}:
            print('*',end=' ')
        else:
            print('',end=' ')
    print()'''

i=0

while i<=10:
    print(i)
    i=i+1