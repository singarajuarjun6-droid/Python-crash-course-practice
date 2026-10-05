# text - based feedback analyzer 


# paragraph input from the user
user_para = input("enter the paragraph :")

#upper and lower case 
print("\n",user_para.upper())
print("\n",user_para.lower())

#check for a word or phrase ex ( the )
is_the = ("the" in user_para)or("The" in user_para)
print("the value (the) is present",is_the)
if is_the == True :
    print("position of (the) :",user_para.find("the") or user_para.find("The"))

#change the with -x-
user_new_para = user_para.replace("the","-x-").replace("The","-x-")
print("\n",user_new_para)
