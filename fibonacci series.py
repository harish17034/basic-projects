a=int(input('enter the terms'))
f=0
s=1
if a<=0:
    print('the number of terms is \n',f)
else:
    print(f,s,end= " ")
    for x in range (2,a):
        next=f+s
        print(next,end= " ")
        f=s
        s=f