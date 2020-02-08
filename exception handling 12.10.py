'''a=eval(input("Enter first number"))
b=eval(input("Enter second number"))
try:
    print(a/b)
except ZeroDivisionError:
    print("Cant divide by 0")
except ValueError:
    print("Enter int value")
except TypeError:
    print("DONT enter words")
except NameError:
    print("Put right name")

a = eval(input("Enter first number"))
b = eval(input("Enter second number"))
try:
    print(a / b)
    try:
        if a==b:
                print("nos are equal")
    except:
        pass
        print("Handled internal")
except:
    pass
    print("handled extrnal")

a = eval(input("Enter first number"))
b = eval(input("Enter second number"))
try:
    print("outer try")

    try:
        print("inner try")
        if a>b:
            print("Greater no")
        else:
            print("Smaller no")
    except:
        print("inner except")
    finally:
        print("inner finally")
except:
    print("outer except")
finally:
    print("outer finally")

a = eval(input("Enter first number"))
b = eval(input("Enter second number"))

try:
    if a==b:
        print("nos same")

    else:
        print("nos not same")
    print(a / b)
except:
    print("Handled")
else:
    print("SOmething else")

finally:
    print("done")
"finally and else and generalised except only once allowed"

try:
    print("hi")
except ZeroDivisionError:
    pass
except:
    pass

try:
    print(10/0)
except ZeroDivisionError as msg:
    print(msg)'''

try:
    print("trying")
    try:
        print("trying2")
        try:
            print("trying3")
        except:
            pass
        else:
            print("SOmething else3")

        finally:
            print("done3")
    except:
        pass
    else:
        print("SOmething else2")

    finally:
        print("done2")
except:
    pass
else:
    print("SOmething else1")

finally:
    print("done1")