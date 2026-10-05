# College Admission Eligibility System

# student's age, entrance exam score, intermediate percentage, and chosen course.
s_age = int(input("enter the age :"))
s_entrance_exam_score = int(input("enter the score in entrance exam :"))
s_inter_percentage = int(input("enter the inter % :"))
s_course = input("enter the selected course :")

#scholarship %
scolar = 0
if(s_entrance_exam_score >= 90)and(s_inter_percentage >95):
    scolar = 25 
print("scholarship :",scolar)

#check eligibility cse and ece and ai (3 courses available)
course = "none"
if(s_entrance_exam_score >75)and(s_entrance_exam_score <=85):
    course = "ece"
    print(course)
elif(s_entrance_exam_score >85)and(s_entrance_exam_score <=95):
    course = "cse"
    print(course)
elif(s_entrance_exam_score>90):
    course = "ai"
    print(course)
else :
    print("not elegible")