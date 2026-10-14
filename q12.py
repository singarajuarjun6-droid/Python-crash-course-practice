students = {
    101: {"name": "Arjun", "marks": 50},
    102: {"name": "Rahul", "marks": 150},
    103: {"name": "Ananya", "marks": 50}
}

# display all the students 

print("all the students :")
for roll,info in students.items():
    print(f"Roll of student :{roll} | name : {info['name']} | marks : {info['marks']}")

# search for a student using roll number 

search_r_n = int(input("enter the roll number to search :"))
if search_r_n in students:
        found = students[search_r_n]
        print(f"Found : \nDetails - roll :{search_r_n} - name {found['name']} - marks {found['marks']}")
else:
     print("---- not found ----")   

# add a new student 

new_roll = int(input("enter the roll number of new Student :"))
new_name = input("enter name :")
new_marks = int(input("enter the marks :"))

students[new_roll] = {'name':new_name,'marks':new_marks}

for roll , info in students.items():
    print(f"Roll : {roll} | name : {info['name']} | marks : {info['marks']}")

# update a students marks

search_update = int(input("enter the roll number to upadate"))

if search_update in students:
     print("enter the new data :")
     update_name = input("enter the updated name :")
     update_marks = int(input("enter the updated marks :"))
     students[search_update] = {'name':update_name,'marks':update_marks}
     for roll , info in students.items():
          print(f"Roll : {roll} | name : {info['name']} | marks : {info['marks']}")
else:
     print("----- try again -----")

# student with the highest marks

high = -1
top = None
for info in students:
     found = students[info]
     if found['marks']> high:
          high = found['marks']
          top = found['name']
print(f"top student : {top} , marks : {high}")

# average marks and above 80
avg = 0
count = 0
count_80 = 0
for info,value in students.items():
     if(value["marks"]>80):
          count_80 += 1
     avg=avg+value["marks"]
     count+=1

print(avg/count)
print(count_80)