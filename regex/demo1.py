import re 

text = "Hello from simple Regex demo"
pattern = f"Hello"

# i want ot check hello is start of my statement
match=re.match(pattern,text)
if match:
     print("Text started with Hello")
else:
     print("Text not started with Hello")


# check something from entire string
search=re.search(r"ERROR","This is log Error....")
if search:
     print("text includes Error")
else:
     print("text not includes error")     


