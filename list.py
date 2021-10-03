#list
marks=[90,98,87,45,67]  #also using negative index
marks[0],marks[-1]=marks[-1],marks[0]
for i  in range(len(marks)):
	print(marks[i])
for m in marks:
	print(m,end=" ")
