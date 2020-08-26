# 人数と点数を読み込んで最低点・最高点を表示(その２：組み込み関数を利用）

print('最低点と最高点を求めます。')

number = 0
tensu = []

while True:
    s = input('{}番の点数:'.format(number+1))
    if s == 'End':
        break
    tensu.append(int(s))
    number += 1

minimum = min(tensu)
maximum = max(tensu)

print('最低点は{}点です。'.format(minimum))
print('最高点は{}点です。'.format(maximum))
