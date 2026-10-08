# Student Marks Analyzer

marks = [78, 92, 65, 92, 88, 71, 65, 95,78, 92, 65, 92, 88, 71, 65, 95] 

high = max(marks)
low = min(marks)
avg = sum(marks)/len(marks)

print("High :",high)
print("low :",low)
print("average :",avg)

above_75 = 0
for i in marks:
    if(i>=75):
        above_75+=1

print("above 75 :",above_75)

below_50 = 0
for i in marks:
    if(i<=50):
        below_50+=1

print("below 50 :",below_50)

unique_set = set(marks)
print(unique_set)

reverse = marks[::-1]
print(reverse)

#search for an element 
search = int(input("enter a number to search :"))
print(search in marks)