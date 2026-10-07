#pattern generator

n = int(input("enter the value of n :"))

print("\nprint 1 :",end="")

for i in range(0,n):
    for j in range(0,i):
        print("*",end="")
    print("")


print("print 2 :",end="\n")

for i in range(0,n):
    for j in range(0,n-i):
        print("*",end="")
    print("")

print("print 3 :",end="\n")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    
    print("")

print("print 4 :",end="\n")

for i in range (1,n+1):
    for j in range (1,i+1):
        print(i,end="")
    print("")