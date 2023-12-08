N = input()
ans = 0

# 2進数から10進数への変換はA04-Binary Representation 1.pyと異なり、鉄則本の意図を汲み取りました。
# int関数でサクッと終わらせる方法もあります。一応、どちらかは実装しておいたほうが経験になります。
for i in range(len(N)):
  if N[len(N)-i-1] == str(1):
    ans += 2 ** i
print(ans)