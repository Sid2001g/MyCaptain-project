term=int(input("Enter number of terms:"))
x,y=0,1
z=0
if term<=0:
    print("Enter positive integer")
elif term==1:
    print("sequence upto",term,":")
    print(x)
else:
    print("Sequence:")
    while z<term:
        print(x)
        a=x+y
        x=y
        y=a
        z+=1
