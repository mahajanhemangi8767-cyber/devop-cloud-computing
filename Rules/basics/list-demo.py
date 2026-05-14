my_list=[1,2,3,4,5,6,7]
print(my_list)
print(f"Item at index 3: {my_list[3]}")


my_list[2]=33
print(my_list)

# add new
my_list.append(8) # insert at least index 
print(my_list)

# insert at index
my_list.insert(2,3) # at index 2 insert value 3
print(my_list)

# remove 
my_list.remove(3) # remove value
print(my_list)
 
my_list.pop() # remove last element
print(f"After remove:{my_list}")

my_list.pop(4) # remove from index 4
print(f"after remove:{my_list}")


print(f"Length: {len(my_list)}")
#loop
for num in my_list:
    print(num)


