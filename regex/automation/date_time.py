from datetime import datetime,date

now=datetime.now()

print("Date & Time: ",now)
print("Date:",now.date())
print("Year:",now.year)
print("Month:",now.month)
print("Day:",now.day)
print("Hour:",now.hour)
print("Minute:",now.minute)

myday = date.today()
print(myday)

print("Default date and time: {now}")
# Formating
print(f"format: {now.strftime("%d/%m/%Y %H:%M:%S")}")
# convert date into string
# convert string to date object 
# use parse: strptime
date_str="2025-05-03" # This is string
date_ob=datetime.strptime(date_str,"%Y-%m-%d")
print(date_ob)





