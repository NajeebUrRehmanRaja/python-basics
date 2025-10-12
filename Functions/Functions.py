from pyclbr import Function


def hello_func():
    pass 
hello_func()

def hello_func():
    pass
print(hello_func())


def hello_func():
    print("Hello function")

print("Hello function")
print("Hello function")
print("Hello function")
print("Hello function")


def hello_func():
    print("Hello function")

hello_func()
hello_func()
hello_func()
hello_func()

def hello_func():
    return "Hello function"
    

print(hello_func())

def hello_func():
    return "Hello function"
    

print("\n" + hello_func().upper())

def hello_func(greeting):
    return '{} Function.'.format(greeting)
    
print("\n" + hello_func("Hey!"))

def hello_func(greeting, name="You"):
    return '{}, {}'.format(greeting, name)
    
print("\n" + hello_func("Hey!", name = "Najeeb"))