# two number calculator

#user data 
num_1 = int(input("enter the 1st digit :"))
num_2 = int(input("enter the 2nd digit :"))
if num_2>=0 :
    print("1)addition\n2)subtraction\n3)multiplication\n4)division\n5)floor division\n6)remainder\n7)exponentiation")
    value = int(input("enter the operation no. from above :"))

if(value == 1):
    print(num_1+num_2)
elif(value == 2):
    print(num_1-num_2)
elif(value == 3):
    print(num_1*num_2)
elif(value == 4):
    print(num_1/num_2)
elif(value == 5):
    print(num_1//num_2)
elif(value == 6):
    print(num_1%num_2)
elif(value == 7):
    print(num_1**num_2)
else:
    print("invalid selection")

if(num_2==0):
    print("enter again")
