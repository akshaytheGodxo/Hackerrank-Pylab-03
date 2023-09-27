h = int(input())
w = int(input())

for i in range(h):
    for j in range(h, i, -1):
        print(" ",end="")
    for k in range(2*i +1):
        if k == 0 or k == 2*i or i == w:
            print("*",end="")
        else:
            print(" ",end="")
    print()