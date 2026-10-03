# take 3 products as inpuut , print total bill + average bill 

nums = []

for i in range(3):
    value = int(input("enter the value :"))
    nums.append(value)

print(nums)
total = 0 

for i in nums:
    total = total + i 

print("total amount : ", total)
print("average : ", total/3)