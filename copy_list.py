import copy
l1=[[10,20,30],[40,50,60],[70,80,90]]
print(id(l1))
l2=copy.copy(l1)
print(id(l2))
l1[1][2]='abcd'
print(l2)
