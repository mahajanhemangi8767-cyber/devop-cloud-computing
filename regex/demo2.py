import re

text = "contact me at dev@pw.com or admin@pw or sonam.soni@pw.com"
pattern= r"[A-za-z0-9._-]+@[A-za-z0-9._-]+\.[A-Za-z]{2,3}"

# pattern for email
emails = re.findall(pattern,text)

# find all values which match with this pattern given in text  
print(emails)




