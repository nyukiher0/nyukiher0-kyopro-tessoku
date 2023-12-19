T = int(input())
N = int(input())

S = [0] * (T+1)

for _ in range(N):
    L,R = map(int,input().split())
    S[L] += 1
    S[R] -= 1

for i in range(1,T+1):
    S[i] += S[i-1]

for i in range(T):
    print(S[i])