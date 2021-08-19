# 지하철 칸별로 10명, 20명, 30명

subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

# 조세호가 몇 번째 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈을 유재속 조세호 사이에 태움
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway.count("유재석"))

lst = [5,4,3,2,1,0]
lst.sort()
print(lst)

# 순서 뒤집기
lst.reverse()
print(lst)

# 모두 지우기
#lst.clear()
#print(lst)

# 다양한 자료형 함께 사용
mlst = [1,True,"나다"]
print(mlst)

# 리스트 확장
lst.extend(mlst)
print(lst)