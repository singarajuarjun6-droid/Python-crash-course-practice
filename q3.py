# student performance report generator

#student data

s_name = input("enter student name :")
s_roll_no = int(input("enter student roll no. :"))
s_branch = input("enter student branch :")
s_sem = int(input("enter the sem :"))

#marks of five subjects out of 100 ( obtained )
s_sub_1 = int(input("marks of sub_1 :"))
s_sub_2 = int(input("marks of sub_2 :"))
s_sub_3 = int(input("marks of sub_3 :"))
s_sub_4 = int(input("marks of sub_4 :"))
s_sub_5 = int(input("marks of sub_5 :"))

#marks of five subjects out of 100 ( target )
t_sub_1 = int(input("Target (%) sub_1 :"))
t_sub_1_marks = (t_sub_1/100)*100
diff_1 =  t_sub_1_marks  - s_sub_1

t_sub_2 = int(input("Target (%) sub_2 :"))
t_sub_2_marks = (t_sub_2/100)*100
diff_2 =  t_sub_2_marks  - s_sub_2

t_sub_3 = int(input("Target (%) sub_3 :"))
t_sub_3_marks = (t_sub_3/100)*100
diff_3 =  t_sub_3_marks  - s_sub_3

t_sub_4 = int(input("Target (%) sub_4 :"))
t_sub_4_marks = (t_sub_4/100)*100
diff_4 =  t_sub_4_marks  - s_sub_4

t_sub_5 = int(input("Target (%) sub_5 :"))
t_sub_5_marks = (t_sub_5/100)*100
diff_5 =  t_sub_5_marks  - s_sub_5

print("Student name :",s_name,"\n","roll no. :",s_roll_no,"\n","branch :",s_branch,"\n","sem :",s_sem)
print("Sub 1 marks :",s_sub_1,"|","taget :",t_sub_1,"|","percentage obtained :",(s_sub_1*100/100),"|","diff marks:",diff_1)
print("Sub 2 marks :",s_sub_2,"|","taget :",t_sub_2,"|","percentage obtained :",(s_sub_2*100/100),"|","diff marks:",diff_2)
print("Sub 3 marks :",s_sub_3,"|","taget :",t_sub_3,"|","percentage obtained :",(s_sub_3*100/100),"|","diff marks:",diff_3)
print("Sub 4 marks :",s_sub_4,"|","taget :",t_sub_4,"|","percentage obtained :",(s_sub_4*100/100),"|","diff marks:",diff_4)
print("Sub 5 marks :",s_sub_5,"|","taget :",t_sub_5,"|","percentage obtained :",(s_sub_5*100/100),"|","diff marks:",diff_5)



