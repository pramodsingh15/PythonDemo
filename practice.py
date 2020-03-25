firstName = "Pramod "
secondName = "Singh "
name = firstName + secondName + str(2)
print(name)
print(type(firstName))

a = 10
print(a)
print(id(a))
b = 10
print(id(b))
a = -10
print(a)
print(id(a))
print(type(a))
g = 10.45
print(g)
h = 5+7j  # complex data type
print(h)
print(type(h))

# list data type
list = [20, 5, 3, 5, 10.2, "Python"]
print(list)
print(type(list))
print(list[2])
list[2] = 4
print(list)

# tuple data type
tuple1 = (1, 2, 4, 3, 4, 5.2, "Hello")
print(tuple1)
print(type(tuple1))
# tuple1[1] = 3 #'tuple' object does not support item assignment
