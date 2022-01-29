from itertools import count


lst = list(map(int,input().split()))
s = set(lst)

cnt = 0
for i in s:
    if lst.count(i) >= 2:
        cnt += lst.count(i)//2
    else:
        continue
print(cnt)