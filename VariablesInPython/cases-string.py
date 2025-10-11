#  we can find the string by case
message = "Hello Python World"
print(message.upper())
print(message.lower())
print(message.title())
#  we can find the string by case in reverse order
print(message.swapcase())

# we can count the number of times a substring appears in a string
print(message.count("l"))
#  we can replace the string
print(message.replace("Python", "Java"))
#  we can find the index of the first occurrence of a substring in a string
print(message.find("Python"))