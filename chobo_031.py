# 31
a = "3"
b = "4"
print(a+b) #34

# 32
print("Hi"*3) #HiHiHi

# 33
print("-"*80)

# 34
t1 = "python"
t2 = "java"
print((t1+" "+t2)*4)

# 35
# print 포메팅에서 '%s'는 문자열 데이터 타입의 값을 '%d'는 정수형 데이터 타입 값을 출력함
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이 %d" % (name1, age1))
print("이름: %s 나이 %d" % (name2, age2))

# 36
# 문자열 포멧 메서드는 타입과 상관없이 값이 출력될 위치에 '{}'를 적어주면 됨
print("이름: {} 나이: {}".format(name1,age1))
print("이름: {} 나이: {}".format(name2,age2))

# 37 
# f-string (파이썬 3.6이후 지원)
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 38
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(",","")
상장주식수 = int(상장주식수)
print(type(상장주식수))

# 39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 40
data = "    Samsung    "
data = data.strip()
print(data)

