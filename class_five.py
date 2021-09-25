#Tuple
# t1 = (False, True,100)
# t2 = (1,4,9)
# t3 = t1 + t2
# print(t1)


# t1 = (False,True,100) #we can not delete from the tuple
# del(t1)
# print(t1)

#update()
# s = {"True","Born",45,"Water"}
# b = {"mary","favour","Tunde",50}
# u = s.union(b)
# print(u)
# s.update(b)
# print(s) 

# a = {"True","Born",45,"Water"}
# b = {"mary","favour","Tunde",50}
# #u = s.union(b)
# #print(u)
# #s.update(b)
# #print(s) 
# print(a.difference(b))
# print(b.difference(a))
# print(a.symmetric_difference(b))# it will join a.differnce(b), b.difference(a) and add them in one set

#intersection
set1= {10,20,30,40,50}
set2 = {30,40,50,60,70}
set3 = set1.intersection(set2)
print(set3)

#union
# set1= {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# set3 = set1.union(set2)
# print(set3)

# set1= {10,20,30}
# set2 = {20,40,50}
# set1.difference_update(set2)
# #set1.update(set2)
# print(set1)

#given two python sets , update the first set with items that exist only in the
#remove items 10,20,30 from the following set at once
# set1  = {10,20,30,40,50}
# set1.difference_update({10,20,30})
# print(set1)

# set1= {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# print(set1.symmetric_difference(set2))
# set1.difference_update(set2)
# #set1.update(set2)
# print(set1)

#remove items from set 1  that are not common to set1 and b
# set1= {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# print(set1.intersection_update(set2))

#remove items from set 1  that are not common to set1 and 2
# set1= {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# set1.intersection_update(set2)
# print(set1)

# from decimal import Decimal
# arr=[1,1,0,-1,-1]
# positive= []
# negative= []
# zero = []

# for i in arr:
#     if i>0:
#       positive.append(i)
#     elif i<0:
#         negative.append(i)
#     else:
#         zero.append(i)
# positive_ratio = len(positive)/len(arr) 
# negative_ratio = len(negative)/len(arr) 
# zero_ratio = len(zero)/len(arr)

# print(round(Decimal(positive_ratio), 6))
# print(round(Decimal(negative_ratio), 6))
# print(round(Decimal(zero_ratio), 6))
