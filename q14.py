# Student performance system 

students = {}
subjects = ["sub_1","sub_2","sub_3","sub_4","sub_5"]

#add student
def add_student():
    new_name = input("enter the name :")
    new_roll = int(input("enter the roll :"))
    new_sub_1 = int(input("marks sub_1 :"))
    new_sub_2 = int(input("marks sub_2 :"))
    new_sub_3 = int(input("marks sub_3 :"))
    new_sub_4 = int(input("marks sub_4 :"))
    new_sub_5 = int(input("marks sub_5 :"))
    students[new_roll] = {"name":new_name,"sub_1":new_sub_1,"sub_2":new_sub_2,"sub_3":new_sub_3,"sub_4":new_sub_4,"sub_5":new_sub_5}


#calculate_total()
def calc_total(roll):
    sum = 0
    for sub in subjects:
        sum = sum + students[roll][sub]
    return sum
    



#calculate_average()
def cacl_avg(roll):
    sum = 0
    count = 0
    for sub in subjects:
        sum = sum + students[roll][sub]
        count+=1
    return (sum/count)


#find_highest()
def calc_high(roll):
    high = -1
    for sub in subjects:
        if (students[roll][sub] >= high):
            high = students[roll][sub]
    print(f"high :{high}")

#find_lowest()
def calc_low(roll):
    low = students[roll]["sub_1"]
    for sub in subjects:
        if(students[roll][sub] <= low):
            low = students[roll][sub]
    print(f"Low :{low}")


add_student()
print(students)
sum=calc_total(114)
print(f"Sum is :{sum}")
avg = cacl_avg(114)
print(f"Avg is :{avg}")
calc_high(114)
calc_low(114)