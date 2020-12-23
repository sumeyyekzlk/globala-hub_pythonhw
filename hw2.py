firstname=input ("First Name=")
lastname=input("Last Name=")
age=int(input("Age="))
birth=int(input("Date of birth(just year)="))
userinfo=[firstname,lastname,age,birth]
print("User's Informations:")
for i in userinfo:
	print(i)
if age<=18:
	print("You can't go outside because it's too dangerous!!!")
else:
	print("You can go out to the street.")
