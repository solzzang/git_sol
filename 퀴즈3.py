url = "http://google.com"
a = url.replace("http://","")
b = a[-4:]
c = a.replace(b,"")

print(c[:3]+str(len(c))+str(c.count("e"))+"!")