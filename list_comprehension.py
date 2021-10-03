#numbers👇️
l=[no for no in range(1,11)]     #no*2 ,no**2,etc..
print(l)
#output: [1,2,3,4,5,6,7,8,9,10]
l1=[10,20,30,40]
l2=[30,40,50,60]
l3=[no for no in l1 if not in l2]
print(l3)
#output: [10,20]


#string👇️
l1="today is thursday"
words=l1.split()
print(words)
l2=[word.upper(),len(word)] for word in words]
print(l2)

#output:
#['today', 'is', 'thursday']
#[['TODAY', 5], ['IS', 2], ['THURSDAY', 8]]
