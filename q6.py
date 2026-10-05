# simple username and password checker

#user input 
username = input("enter the user name :")
email = input("enter the email.id :")
password = input("enter the password :")

#checks
check_count = 0 # to be 3 to be correct

#username check ( 5 charechters )
if(len(username)>=5):
    check_count+=1
if(("@" in email)and(".com" in email)):
    check_count+=1
if((len(password)>=8)
   and(any(char.isdigit() for char in password))
   and(any(char.isupper() for char in password))):
    check_count+=1

if(check_count==3):
    print("all passed")
else:
    print("Failed")