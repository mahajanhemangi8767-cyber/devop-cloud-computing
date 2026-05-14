import re


with open("app.log") as file:
    for line in file:
        if "ERROR" in line or "CRITICAL" in line:
            print(line.strip())

print("---------------print using match-----------")
pattern=re.compile(r'.* - (ERROR | CRITICAL) - *')
with open("app.log") as file:
    for line in file:
        if pattern.match(line):
            print(line.strip())





