c = input()

l = len(c)
ch = ""
if l%2 == 1:
    print("Odd length.")
else:
    for i in range(0 , l , 2):
        ch += c[i+1] + c[i]

    print(ch)