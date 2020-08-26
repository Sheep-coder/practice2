# ２値の小さい方の値を表示（その2:条件演算子）

a=int(input('整数a:'))
b=int(input('整数b:'))

min2 = a if a < b else b
print('小さいほうの値は',min2,'です。')
