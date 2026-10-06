# number analyzer

n = int(input("enter the value of n :"))

# all numbers , numbers divisble by 3 count
div_3 = 0
print("all numbers 1 - n :")
for i in range(1,n+1):
    print(i)
    if(i%3==0):
        div_3+=1
    else:
        continue

#even numbers 
even_sum = 0
print("even numbers :")
for i in range(1,n+1):
    if(i%2==0):
        print(i)
        even_sum = even_sum + i
    else:
        continue

#odd numbers
odd_sum = 0
print("odd numbers :")
for i in range(1,n+1):
    if(i%2!=0):
        print(i)
        odd_sum = odd_sum + i
    else:
        continue

#odd and even sum
print("even sum :",even_sum)
print("odd_sum :",odd_sum)

print("no. div by 3 in list :",div_3)

#div by 5 , 7 first no.
div_5_7 = -1
for i in range(i,n+1):
    if(i%5==0)and(i%7==0):
        print("the number div by 5 and 7 :",i)
        break

