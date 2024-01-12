lst= [3,3]
ln=len(lst)
trgt=6

for i in range (0,ln):
    for j in range (i+1,ln):
        if lst[i]+lst[j]==trgt:
            print (i,j)

            break
