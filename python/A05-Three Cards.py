N, K = map(int, input().split())
ans = 0

for i in range(1,N+1):
  for j in range(1,N+1):
    rest = K - i - j
    # rest <= N の暗黙の条件に注意ください
    if rest > 0 and rest <= N:
      ans += 1

print(ans)