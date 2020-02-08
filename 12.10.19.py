'''a=(x*x for x in range(10))
print(list(a))

l=['Sakshi','Doshi','Aditya','Kinjal','Shah']
f=[x[0]+x[1] for x in l]
print(f)

list comprehension is supported but tuple comprehension not supported it gives generator obj as result
along w the address

s='the quick brown fox jumps over lazy dog'
f=s.split()
a=[[x.upper(),len(x)] for x in f ]
print(a)'''

'''a={a*a for a in range(10)}
print(a)

a={a:a*a for a in range(10)}
print(a)'''

'generator' \
'generator is a fn but it wont take any func as a input // it is responsible for producing sequence' \
'memory related probs dont occur bs of generator'
'it uses yield keyword instead of return keyword'

'''a=(i*i for i in range(10000000000000000000000000))
print(next(a))
print(next(a))
print(next(a))'''

def fun(num):
    for i in range(num):
        yield(i*i)
    print(fun(1000000000000000000000))

'''z=100
for i in z:
    print(next(i))'''

a=fun(100)
i=0
while i<=10:
    print(next(a))
    i=i+1