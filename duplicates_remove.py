input="ABCDBCADADCB"
l=[]
for letter in input:
	if letter not in l:
		l.append(letter)
else:
	print(l)
	output=" ".join(l)
	print(output)

output="ABCD"
