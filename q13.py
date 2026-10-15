# building own utility function

#is even(number)
def is_even(number):
    if number != 0:
        if number % 2 == 0:
            print(f"number : {number} | EVEN")
        else:
            print(f"number : {number} | NOT EVEN")
    else:
        print(f"number : {number} | NOT EVEN")
    return 0
#count vowels(text)
def is_vowel(text):
    count = 0
    for c in text:
        if c in "AEIOUaeiou":
            count+=1
    if count >= 1 :
        print("YES VOWEL")
    else:
        print("NOT VOWEL")
    return
#find largest(numbers) 
def is_largest(arr):
    high = -1
    for i in arr:
        if i > high:
            high = i
    print("Highest :",high)
    return
#Calc avg(numbers)
def is_avg(arr):
    sum = 0
    count = 0
    for i in arr:
        count += 1 
        sum = sum + i 
    print("avg is :",sum/count)
    return
#is_prime(number)
def is_prime(number):
    if number <= 1:
        print(f"number: {number} | NOT PRIME")
    else:
        for i in range(2,number):
            if number%i == 0 :
                print(f"number: {number} | NOT PRIME")
                return
        print(f"number: {number} | PRIME")


n = int(input("enter the number to check for prime and is_even :"))
is_even(n)
is_prime(n)

textt = (input("enter the text for vowel check :"))
is_vowel(textt)

arr1 = [10,20,30,40,50,60,70]
is_largest(arr1)
is_avg(arr1)
