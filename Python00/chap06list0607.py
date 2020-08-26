# 文字列txt無いに文字列prnは含まれているか

txt=input('文字列txt:')
ptn=input('文字列ptn:')

if ptn in txt:
    print('ptnはtxtに含まれています。')
else:
    print('ptnはtxtに含まれていません。')
