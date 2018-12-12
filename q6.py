# function to return list of those number in range 1 to 50 which is multiple of 2 and 6 both. and calculate the sum of last 3 val

total_sum = 0
n=[]
for i in range(1,51):
    if (i % 2 == 0 or i % 6 == 0):
        n.append(i)
total_sum=sum(n[-3:])
print("List of multiple of 2 and 6::",n)
print("Total sum of last 3 number::",total_sum)

	