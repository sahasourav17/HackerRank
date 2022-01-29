def arrayManipulation(n,queries):
    l = [0]*(n+1)
    for i in range(len(queries)):
        a = queries[i][0]-1
        b = queries[i][1]
        k = queries[i][2]

        l[a] += k
        l[b] -= k

    max_val = 0
    prev = 0
    for i in l:
        prev += i
        max_val = max(max_val,prev)
    return max_val

n,m = map(int,input().split())
queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
result = arrayManipulation(n,queries)
print(result)