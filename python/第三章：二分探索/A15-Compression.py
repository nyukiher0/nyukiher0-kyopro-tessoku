import bisect

N = int(input())
A = list(map(int,input().split()))
ans = [0] * len(A)

unique_A = sorted(list(set(A)))

for i in range(len(A)):
    ans[i] = bisect.bisect_left(unique_A, A[i])
    ans[i] += 1

print(" ".join([str(item) for item in ans]))