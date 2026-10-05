#username and email analyzer

#user data
user_name = input("enter the user full name :")
user_email = input("enter the user email address :")

#display names in uppercase and lowercase
print(user_name.upper())
print(user_name.lower())

#find position of first " "
print("found at position :",user_name.find(" "))

#check if email has @ and .
print("values of (@ and .) are :",(("@" in user_email)and("." in user_email)))

#replace spaces with _
print(user_name.replace(" ","_"))


