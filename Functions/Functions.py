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

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
student_info("Najeeb", "Ahsan", age=22, height=5.10)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ["Math", "Art"]
instructor = {"name": "Mr. Ahsan", "age": 40}

student_info(*courses, **instructor)

# Number of days per month. First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return "Invalid month"
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(days_in_month(2023, 2))
print(is_leap(2016))