num = int(input("Enter number "))

for i in range(2,num):
    if(num%i==0):
        print("Not Prime number")
        break
else:
    print("Prime number")
