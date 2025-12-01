#read input_day1.txt file one line at a time
n=50
c=0
with open('input_day1.txt', 'r') as file:
    for line in file:
        op=line[0]
        num=int(line[1:].strip())

        #if R crank right, if L crank left
        if op=='L':
            res=n-num
            #this controls the case when we cross 0 going left, so under 0
            if res<0 and n!=0:
                c+=1
        elif op=='R':
            res=n+num

        #mul is how many times we crossed 100, so 0
        mul=abs(res)//100
        n=res%100
        #check if we landed on 0 without crossing it (we already counted crossing it)
        if n==0 and not abs(res)//100>0:
            c+=1
        c+=mul
        
print(c)