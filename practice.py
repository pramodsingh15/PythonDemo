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


# range
rg = range(5)
print(rg[0])
print(rg[1])

rgb = range(10, 20, 2)
print(rgb[0])
print(rgb[1])
print(rgb[3])
print(rgb[-1])
print(rgb[-2])
print(type(rgb))

# set
data = {10, 20, 30, "Hello", 1.2, 4.2}
print(data)
print(type(data))
# print(data[0])  can't access with index in set  #'set' object is not subscriptable

data1 = {10, 20, 10, 40, 30, 50, 20}
print(data1)  # set doesn't accept duplicate values

# MAP
mp = {101: "Name", 102: "RollNo", 103: "Subject"}
print(mp)
print(type(mp))
print(mp[101])

# declare and initialize variable
a = b = c = d = 10
print(a)
print(b)
print(c)
print(d)
a = b = c = d = True
print(a)
print(b)
print(c)
print(d)

a, b, c, d = 10, 2.4, "Hello", "World"
print(a)
print(b)
print(c)
print(d)

a = 5
b = 2
value = a < b
print(value)

c  = 2 
d = 3
value = c < d
print(value)

st1 = "HelloWolrld"
a = "to" in st1
print(a)

st2 = "Python"
b = "th" in st2
print(b)


st1 = "HelloWolrld"
a = "to" not in st1
print(a)

st2 = "Python"
b = "th" not in st2
print(b)


