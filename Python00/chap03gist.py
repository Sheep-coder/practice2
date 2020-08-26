# 第３章　まとめ

a = int(input('整数a:'))
b = int(input('整数b:'))
c = int(input('整数c:'))
d = int(input('整数d:'))

if a: print('aはゼロではありません。')
if not b: print('bはゼロです。')

# aとbとcの最初の非ゼロを、１個も無ければｄをｘに代入
x = a or b or c or d
print('x =',x)

if d % c:
    print('ｃはｄの約数ではありません。')
else:
    print('ｃはｄの約数です。')
print('ｃは'+('奇数'if c %2 else '偶数')+'です。')
print('点数ｄの評価：',end='')
if d < 0 or d > 100:
    print('不正な値')
elif d >= 60:
    print('合格')
else:
    print('不合格')
