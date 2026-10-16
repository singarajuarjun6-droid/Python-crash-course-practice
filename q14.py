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
    print(sum)
    



#calculate_average()

#find_highest()

#find_lowest()

#calculate_percentage

#get_grade


add_student()
print(students)
calc_total(114)