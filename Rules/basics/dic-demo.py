# Dictonary stores values in key-value pair
# values can be anything
# keys are unique
# mutable

my_dict={
    "names":"Sonam",
    "age":56,
    "city":"Mumbai"
}

print(my_dict)
my_dict["email"]="hemangi@gmail.com" # add new field
my_dict["age"]=35 # update 

print(f"Updated: {my_dict}")

# iterate
for key,value in my_dict.items(): # for only keys use my_dist.keys(), for values my_dict.values()
    print(f"{key}: {value}")



# Remove
my_dict.pop("age")
print(f"After Delete: {my_dict}")
del my_dict["city"]
print(f"After Delete: {my_dict}")
my_dict.clear() # remove everything
print(f"After Clear: {my_dict}")




