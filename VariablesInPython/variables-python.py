# Here is the code which is print using the variable, we can use the variable to print the message multiple times, 
# and we can change the value of the message as well.
# print the simple statement
message = "Hello World"
print(message)
# We can print the message multiple times
print(message)
print(message)
# We can change the value of the message
message = "Hello Python World"
print(message)

#  /////////////////////////

# we can also use this approach
message = 'Hello World'
print(message)
# but using this approach we have a issue, if i want to print the message with single quote i have to escape >> 'Ali\'s World'. with double quotes we can use single quote
message = "He said, Ali's World!"
print(message)


message = """Hello There, We can print line in multiple lines.
And we can use double quote three times to print the message.
"""
print(message)
