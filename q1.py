#program to return the list in single line containing the cube of the 1st 6 fibonacci series.

a = []
cube=lambda x: x*x*x
for i in range(6) :
        if i <= 1 :
            a.append(i)
        else:
            f = int(a[i-2])+int(a[i-1])
            a.append(f)
print("Fibonacci series::",a)
print ("Cube of Fibonacci series::",list(map(cube,a)))