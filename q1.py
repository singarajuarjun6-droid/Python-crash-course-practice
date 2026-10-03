# person info and money spending details 

#personal detaisl
p_name = input("enter the person name :")
p_age = int(input("enter the age :"))
p_city = input("enter the city :")
p_clg = input("enter clg name :")
p_clg_yead = int(input("enter Year of study :"))

#expenses
p_food_spend = float(input("enter the food amt spend :"))
p_transport_spend = float(input("enter the transport amt spend :"))
p_movie_spend = float(input("enter the amt spend on movies :"))

#allowance 
allowance = int(input("enter allowance amt :"))

#calculation
p_spend = ( p_food_spend + p_transport_spend + p_movie_spend )
balance = ( allowance - p_spend )
avg = ( p_spend / 30 )

print("\nAmount spend :",p_spend,"\nAverage spend :",avg,"\nBalance :",balance)