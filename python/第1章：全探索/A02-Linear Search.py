N, X = map(int, input().split())
A = list(map(int,input().split()))
  
for i in range(len(A)):
  if A[i] == X:
    print("Yes")
    exit()

print("No")