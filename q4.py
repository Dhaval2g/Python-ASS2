# program to concatenate the string of those characters which exist at the even position variable.
n=[]
e=[]
x=1
for i in range(21):
	n.append(i)
	if i%2==0 and i!=0:
		x*=i
		e.append(i)
print("List of 1st 10 even number::",e)
print("Mul of 1st 10 even number::",x)
