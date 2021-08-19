from random import *

all = list(range(1,21))
shuffle(all)


winning = sample(all,4)

print("-- 당첨자 발표 --\n치킨 당청자 : {0}".format(winning[0]))
print("커피 당첨자 : {0}\n-- 축하합니다 --".format(winning[1:]))
