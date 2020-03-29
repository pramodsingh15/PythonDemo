# # if else if

# x = int(input("Enter number "))
# y = x % 2

# if (y==0):
#     print("Even")
# if(y==1):
#     print("Odd")


# a = int(input("Enter number "))
# b = a % 2
# if(b==0):
#     print("Even")
#     if(a>5):
#         print("a is greater")
#     else:
#         print("a is smaller")
# else:
#     print("Odd")



# # if elif else

# x = int(input("Enter number "))

# if(x>40 & x<60):
#     print("Second class")
# elif (x>60 & x<75):
#     print("First Class")
# elif (x>75):
#     print("Distinction")
# else:
#     print("below the marks")



# while loop
# i =1
# while i<=5:
#     print("Hello")
#     i=i+1


# i=1
# while i<=4:
#     print("Google ",end="")
#     j=1
#     while j<=4:
#         print("World ",end="")
#         j=j+1
    
#     i=i+1
#     print()



# print(bin(25))
# print(0b0101)
# print(0o25)
# print(hex(25))
# print(0xf)


# for loop

# a = {"Hello",100,12.4}
# # a = "HELLO"

# for i in a:
#     print(i) 


# for i in range(10):
#     print(i)


# for i in range(11,21,2):
#     print(i)


# for i in range(20,10,-1):
#     print(i)



# break
# av = 5
# x = int(input("Enter number"))
# i=1

# while i <= x:
#     if i>5:
#         print("Out of stock")
#         break

#     print("Candy")
#     i=i+1

# print("Bye")



# continue  skip the numbers divisible by 3 and 5
# for i in range(1,101):
#     if i%3==0 and i%5==0:   
#         continue
#     print(i)

# print("Bye")    


# pass
# for i in range(1,51):
#     if(i%2==0):
#         pass
#     else:
#         print(i)

# print("Bye")



# for-else

nums = [10,21,24,26]
for num in nums:
    if(num % 5 == 0):
        print(num)
        break
else:
    print("not found")