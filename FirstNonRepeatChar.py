s="loveleetcode"
cnt=[0]*(26)
for i in s:
    cnt[ord(i)-97]+=1

ind=-1
for i,c in enumerate(s):
    if cnt[ord(c)-97] ==1:
        ind=i
        break    

print(ind)