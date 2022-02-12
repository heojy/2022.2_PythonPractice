site = input("사이트의 URL을 입력해 주세요 : ") #http://naver.com

password_1 = site[7:site.index(".")]

password = password_1[:3] + str(len(password_1)) + str(password_1.count("e")) + "!@#"

print(password)

