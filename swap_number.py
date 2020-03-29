a = int(input("Enter number "))
b = int(input("Enter number "))

print("Before swapping a-->"+str(a))
print("Before swapping b-->"+str(b))

# temp = a
# a = b
# b = temp


# swap no without using third variable
# a = a + b
# b=  a - b
# a = a - b


a,b = b,a

print("After swapping a-->",end="")
print(a)
print("After swapping b-->",end="")
print(b)