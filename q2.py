#smart shopping bill genrator 

#products and details 

#p1
p1_name = input("enter name of product 1 :")
p1_qty = int(input("enter qty of product 1 :"))
p1_price = float(input("enter the price of product 1 :"))

p1_total_price = (p1_qty * p1_price)

#p2
p2_name = input("enter name of product 2 :")
p2_qty = int(input("enter qty of product 2 :"))
p2_price = float(input("enter the price of product 2 :"))

p2_total_price = (p2_qty * p2_price)

#p3
p3_name = input("enter name of product 3 :")
p3_qty = int(input("enter qty of product 3 :"))
p3_price = float(input("enter the price of product 3 :"))

p3_total_price = (p3_qty * p3_price)

#total bill and all 
total_bill = round( p1_total_price + p2_total_price + p3_total_price,2)

#discount and gst 
discount = int(input("enter the (%) of the discount :"))
after_gst = round( total_bill - (total_bill*0.18),2)
after_discount = round(after_gst - (after_gst*(discount/100)),2)


print("Product 1 :",p1_name," | ","QTY :",p1_qty," | ","Sub-price :",p1_price," | ","total_p1 :",p1_total_price)
print("Product 2 :",p2_name," | ","QTY :",p2_qty," | ","Sub-price :",p2_price," | ","total_p2 :",p2_total_price)
print("Product 3 :",p3_name," | ","QTY :",p3_qty," | ","Sub-price :",p3_price," | ","total_p3 :",p3_total_price)
print("\nTotal price :",total_bill)
print("\nafter gst price (18%) :",after_gst)
print("\nfinal price in store :",after_discount)

