#  Comparison
# Equal: "="
# Not Equal: "!="
# Greater Than: ">"
# Less Than: "<"
# Greater Than or Equal To: ">="
# Less Than or Equal To: "<="
# Object Identity: "is" and "is not"

Language = "Python"
Language = "Java"
if Language == "Python":
    print("\n Python is a great language!")
    print("\n I love Python!")
elif Language == "Java":
    print("\n Java is a great language!")
else:
    print("\n I don't know that language.")


# Array
# Check if "Python" is in the array
Language = ["Python", "Java"]
if "Python" in Language:
    print("\n Python is a great language!")
    print("\n I love Python!")
elif "Java" in Language:
    print("\n Java is a great language!")
else:
    print("\n I don't know that language.")

# Bolean Operation 
# And, Or, Not
# And: "and"
# Or: "or"
# Not: "not"


#  Check if user is Admin and logged in (And operator)
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print("\n Admin Page")
else:
    print("\n Bad Credentials")

user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print("\n Admin Page")
else:
    print("\n Bad Credentials")

# Check if user is Admin or logged in (Or operator)
user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
    print("\n Admin Page")
else:
    print("\n Bad Credentials")

# Check if user is not logged in (Not operator)
user = 'Admin'
logged_in = False

if not logged_in:
    print("\n Please log in")
else:
    print("\n Welcome")

#  Flase values
    #  False
    #  None
    #  Zero of any numeric type
    #  Any empty sequence. For example, '', (), [].
    #  Any empty mapping. For example, {}.

condition = False
if condition:
    print("\n This is True")
else:
    print("\n This is False")

condition = None
if condition:
    print("\n This is True")
else:
    print("\n This is False")

condition = 0
if condition:
    print("\n This is True")
else:
    print("\n This is False")

condition = 10
if condition:
    print("\n This is True")
else:
    print("\n This is False")

condition = []
if condition:
    print("\n This is True")
else:
    print("\n This is False")

condition = {}
if condition:
    print("\n This is True")
else:
    print("\n This is False")

condition = ''
if condition:
    print("\n This is True")
else:
    print("\n This is False")

condition = 'Test'
if condition:
    print("\n This is True")
else:
    print("\n This is False")