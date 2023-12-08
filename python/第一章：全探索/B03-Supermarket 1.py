N = int(input())
A = list(map(int,input().split()))

for i in range(N):
# jはi+1から始めることに注意してください
  for j in range(i+1,N):
    # kはj+1から始めることに注意してください
    for k in range(j+1,N):
      if A[i] + A[j] + A[k] == 1000:
        print("Yes")
        exit()
    
print("No")