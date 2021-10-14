l=[23,45,78,34,20,40,28]
i=1
for i in range(1,len(l)):
	for i in range(1,len(l)-i):
		if l[i]>l[i+1]:
			l[i],l[i+1]=l[i+1],l[i]
else:
	print(l)  #-->[23, 20, 28, 34, 40, 45, 78]
