def foo():
    print(x)

def bar():
    global x
    x = 999999999999

x = 345

bar()
foo()

