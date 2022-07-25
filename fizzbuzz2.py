a=int(input("enter the number "))
if(a%3==0 and a%5==0):
    print("FIZZBUZZ")
elif(a%3==0):
    print("FIZZ")
elif(a%5==0):
    print("BUZZ")
else:
    print(a)            