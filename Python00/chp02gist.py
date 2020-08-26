print('ABC','XYZ')
print('ABC','XYZ',end='')
print('ABC','XYZ',sep='')
print()
print('ABC\n\nXYZ',sep='')
print()

s=input('文字列:')
print('あなたは',s,'と入力しました。')

print('あなたは'+s+'と入力しました。')
print('あなたは{}と入力しました。'.format(s))
print()

no=int(input('正の整数値：'))
print('最下位桁:',str(no%10),sep='')
print('２進:'+bin(no))
print('８進:'+oct(no))
print('10進:'+str(no))
print('16進:'+hex(no))
print()

PI=3.14159   # 円周率を表す定数

print('長方形と円の面積を求めます。')
width=float(input('長方形の横幅:'))
height=float(input('長方形の高さ'))
radius=float(input('円の直径:'))

print('長方形:{}'.format(width*height))
print('円　　:{}'.format(PI*radius*radius))

