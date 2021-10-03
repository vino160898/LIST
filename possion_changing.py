#possition changing

l1=['tokyo','berlin','rio','denver']
l2=[101,102,103,104]
students=[l1,l2]
print(students)
for i in range(len(students)):
	for j in range(len(students[i])):
		if i==0 and j==1:
			students[i][j]='raquel murillo'
print(students)
