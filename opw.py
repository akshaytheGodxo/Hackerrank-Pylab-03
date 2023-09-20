'''
In this Programme , We have to take 3 things as input from the User : 
1. The main String value
2. The place holder Value
3. Value to repeat the new reversed integer 

We will use the place holder value to slice our string in two part and then we will swap the place values of both substrings 

Then we will repeatidly print the reversed substring value 

We can also use array / list method to reverse it as it becomes easier

Note. 
1. Make sure there is space between all of the letters in the final String 
2. Also if there is a space in the inital string , you have to ignore that :D
Enjoy the Code :D
'''
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
    
            
