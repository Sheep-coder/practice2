# 数当てゲーム

import random

MAX = 1000
MAX_STAGE = 10
print('１～{}の数を{}回以内で当てて下さい。'.format(MAX,MAX_STAGE))

stage = 1
answer = random.randint(1,MAX)

while stage <= MAX_STAGE:
    print(stage,'回目　いくつかな:',end='')
    n = int(input())

    if n < 1 or n > MAX:
        continue
    if n == answer:
        print('正解。',stage,'回で当たりました。')
        break
    elif n > answer:
        print('もっと小さな数です。')
    else:
        print('もっと大きな数です。')

    stage += 1

else:
    print('残念。正解は',answer,'でした。')
