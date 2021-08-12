from random import *

print(random()) # 0.0~1.0 랜덤 수
print(random()) # 0,0~10.0
print(int(random()*10))# 0~10 미만의 랜덤 값
print(int(random()*10)+1)# 0~10 이하의 랜덤 값


print(int(random()*50)+1)

print(randrange(1,46)) #1~46 미만의 랜덤 값
print(randint(1,45)) #1~45 이하의 랜덤 값