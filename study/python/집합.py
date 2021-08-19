# set 중복 불가 , 순서 없음
my_set ={1,3,2,5,4}
print(my_set)

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java를 할 수 있지만 python을 모르는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 수 있는 사람이 늘어남ㅁ
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)

