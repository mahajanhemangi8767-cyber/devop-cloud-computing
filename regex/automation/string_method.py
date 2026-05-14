# creating strings

str1 = "Hello"
str2 = "World"
str3 = "This is my multiliner string"

print(str3)
print(f"This is my string: {str1} {str2}")

greeting = str1 + " " + str2 # concat
print(greeting)

# Repeat string
print((str1 + " ") * 5)

# string slicing
print(greeting[0:5])
print(greeting[6:])  # corrected index

# replace
print("replace:", str1.replace("H","W"))

# convert
print("upperCase:", str1.upper())
print("lowerCase:", str1.lower())

# string length
print("Length:", len(greeting))

# check
print("python".startswith("py"))
print("python".endswith("on"))


print(len("          hello         "))
print(len("          hello         ".strip())) # removing extra space 


statement = "Ny name is sonam soni and i am a content creator"

words=statement.split() # split with space 

print("-".join(words))    






