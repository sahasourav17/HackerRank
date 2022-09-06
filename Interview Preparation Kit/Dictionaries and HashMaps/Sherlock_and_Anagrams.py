from collections import defaultdict

# iterative approach (finding pair)
def solve_iter(s):
    cnt = 0
    for i in range(1,len(s)):
        for j in range(len(s)-i):
            pair = sorted(s[j:j+i])
            for k in range(j+1,len(s)-i+1):
                if pair == sorted(s[k:k+i]):
                    cnt += 1
    return cnt

#using hashmap
def solve(s):
    cnt = 0
    d = defaultdict(lambda:0)
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            pair = "".join(sorted(s[i:j]))
            cnt += d[pair]
            # print(f'pair: {pair} and value : {d[pair]}')
            d[pair] += 1
    return cnt

for _ in range(int(input())):
    s = input()
    print(solve(s))