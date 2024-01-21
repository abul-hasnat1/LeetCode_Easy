# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string
strs=["flower","flow","flight"]
prefix=''
lst_len= len(strs)
low_len=201

if lst_len==1:
    prefix=strs[0]

else:
    for i in  range (lst_len):
        if len(strs[i])<low_len:
            low_len=len(strs[i])

    count=0
    for j in range(low_len):
        if count+1<lst_len:
            if strs[count][j]==strs[count+1][j]:
                prefix+=strs[count][j]
                count+=1
        

        

print(prefix)