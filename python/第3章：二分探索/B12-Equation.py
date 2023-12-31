def f(x):
	return x*x*x + x

N = int(input())

# 二分探索
Left = 0.0
Right = 100.0
EPUSITON = 0.001
Mid = (Left + Right) / 2

while(abs(f(Mid) - N) > EPUSITON):
	Mid = (Left + Right) / 2
	val = f(Mid)

	# 探索範囲を絞る
	if val > N:
		Right = Mid # 左半分に絞られる
	else:
		Left = Mid # 右半分に絞られる

# 出力
print(Mid)
