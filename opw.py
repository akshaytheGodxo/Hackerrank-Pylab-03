c = input()
m = int(input())
n = int(input())
d = ""
a = ""

d += c[m:len(c)]
a += c[0:m]

sum1 = d +a
l=[]
for i in sum1:
    l.append(i)

j=0
for i in range(0,n):
    while j <len(l):
        
        if l[j] != ' ':
            
            print(l[j] , end=' ')
        j += 1
    j = 0
    
            
