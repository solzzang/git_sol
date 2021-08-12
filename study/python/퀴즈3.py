a = "http://naver.com"
b = a.replace("http://","")
b = b[:b.index(".")]
c = b[:3] + str(len(b)) + str(b.count("e")) +"!"


print(f"{a}의 비밀번호는 {c}입니다.")