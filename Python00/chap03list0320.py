# ２値の小さい方の値を表示（その１:if分）

a=int(input('整数a:'))
b=int(input('整数b:'))

if a < b:
    min2 = a
else:
    min2 = b
print('小さいほうの値は',min2,'です。')
