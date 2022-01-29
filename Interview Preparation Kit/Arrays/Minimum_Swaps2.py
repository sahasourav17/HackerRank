def minimumSwaps(ara,n):
    swap = 0
    for i in range(n):
        while i+1 != ara[i]:
            actual_idx = ara[i]-1
            ara[actual_idx],ara[i] = ara[i],ara[actual_idx]
            swap += 1
    return swap

n = int(input())
ara = list(map(int,input().split()))
print(minimumSwaps(ara,n))
