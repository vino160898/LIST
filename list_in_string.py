#string 
l1=['tokyo','nairobi','rio','danver']
l2=[101,102,103,104]
students=l1,l2
for student in students:
	for detail in student:
		if type(detail)==str:
			if detail[0]=='r':    #getting a first letter start 'r' in list elements  --> rio
			#if detail[-1]=='r':  #getting a last letter end 'r' in list elements     --> danver
			#if len(detail)==5:   #getting a 5 letters in the list elements        --> tokyo
				print(detail)


