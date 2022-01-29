def minimumBribes(q,n):
    bribe = 0
    for pos,val in enumerate(q):
        if (val-1) - pos > 2:
            print("Too chaotic")
            return
        for j in range(max(0,val-2),pos):
            if q[j] > val:
                bribe += 1
    print(bribe)

for _ in range(int(input())):
    n = int(input())
    q = list(map(int,input().split()))
    minimumBribes(q,n)
