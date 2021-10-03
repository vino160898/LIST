#input="one owt three ruof"
#output="one two three four"
input="one owt three ruof"
words=input.split()
i=0
l=[]
for word in words:
  if i%2==0:
    l.append(word)
  else:
    l.append(word[::-1])
else:
  print(l)
  output=" ".join(l)
  print(output)
