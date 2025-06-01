words = ["abc","bcd","aaaa","cbc"]
x = "a"
ls=[]
for index,i in enumerate(words):
    if x in i:
        ls.append(index)
print(ls)