# ５人の点数を読み込んで合計点と平均点を求めます。

print('５人の点数の合計点と平均点を求めます。')

tensu1 = int(input('1番の点数:'))
tensu2 = int(input('2番の点数:'))
tensu3 = int(input('3番の点数:'))
tensu4 = int(input('4番の点数:'))
tensu5 = int(input('5番の点数:'))

total = 0
total += tensu1
total += tensu2
total += tensu3
total += tensu4
total += tensu5

print('合計は{}点です。'.format(total))
print('平均は{}点です。'.format(total/5))

