def greeting():
    print("Hello Everyone")

def welcome(name):
    if name=='':
        print("Welcome Guest")
    else:
        print(f"Welcome {name}")    

def add(num1,num2):
    return num1+num2

greeting() # call function 
welcome('')
welcome("Sonam soni")
result=add(3,4)
print("Result:",result)
print("Result",add(5,6)) # calling a function in print
# A function can be defined once and reused times by calling its whenever needed.

