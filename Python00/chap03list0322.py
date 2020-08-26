# ２値の差を表示

a=int(input('整数a:'))
b=int(input('整数b:'))

min2 = a if a < b else b
print('差は',b-a if a < b else a-b,'です。')

