# リストの全要素をenumerate関数で走査（１からカウント）

x = ['John','George','Paul','Ringo']

for i, name in enumerate(x,1):
    print('x[{}] = {}'.format(i,name))
