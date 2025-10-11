#  we can add variables in string
greeting = "Hello"
name = "Python"
message = greeting + " " + name
print(message)

#  we can add variables in string with format method
message = "{} {}".format(greeting, name)
print(message)

#  we can add variables in string with format method in reverse order
message = "{1} {0}".format(greeting, name)
print(message)

#  we can add variables in string with format method in step
message = "{0} {1} {0}".format(greeting, name)
print(message)

#  we can add variables in string with f-string
message = f'{greeting.upper()} {name.lower()}. How are you?'
print(message)