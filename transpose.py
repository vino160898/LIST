#input=[[10,20,30],   | #output=[[10,40,70],
#       [40,50,60],   |         [20,50,80],
#       [70,80,90]]   |         [30,60,90]]

l1=[[10,20,30],[40,50,60],[70,80,90]]
l2=[]
for i in range(len(l1[0])): #len(l1)-is three element,l1[0]-is three values
    row=[]
    for item in l1:
      row.append(item[i])
    l2.append(row)
else:
	print(l1)
	print(l2)
