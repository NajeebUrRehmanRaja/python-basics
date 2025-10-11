# here is the code which is print the length of the array
# we can use the len() function to get the length of the array
# let's see the example

message = "Hello Python World"
# we can get the length of the array using the len() function
print(len(message))


#  we can find the string by index
print(message.index("Python"))

#  we can find the string by slice
print(message[7:12]) 

#  we can find the string by slice
print(message[7:]) 
#  we can find the string by slice
print(message[:12]) 
#  we can find the string by slice 
print(message[:]) 

#  we can find the string by slice in step
print(message[::2]) 
#  we can find the string by slice in reverse order
print(message[::-1]) 
#  we can find the string by slice in step in reverse order
print(message[::-2]) 