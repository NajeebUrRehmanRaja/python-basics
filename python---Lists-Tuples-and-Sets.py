from nt import remove


course = ['Math', 'Physics', 'Chemistry']
course2 = ['English', 'Urdu']
# print courses 
print(course)
# length of courses 
print(len(course)) 
# print by index 
print(course[0])
# print by slice 
print(course[:2])
print(course[2:])


# modyfing list 
course.append('Biology')
print(course)
# insert the list 
course.insert(1, course2)
print(course[1])
# use extend to prevent the array within array 
course.extend(course2)
print(course)
# remove
course.remove('Biology')
print(course)
