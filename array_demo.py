from array import *
 
# vals = array('i',[2,3,-4,9])

# for i in range(len(vals)):
#     print(vals[i])

# for i in vals:
#     print(i)


# arr = array('u',['a','e','i'])

# vals1 = arr.reverse()

# for e in arr:
#     print(e)




arr_num = array('i',[2,4,-8,5,6])
newArray = array(arr_num.typecode,(a for a in arr_num))

for i in newArray:
    print(i)
