#2021 12 20  변수
# 1) 레퍼런스: 값이 저장된 메모리의 위치를 가리키는 레퍼런스(Reference: 참조)
# 2) 동적 타이핑: 값의 형에 따라서 고정되지 않고, 동적으로 자료 유형을 매핑해서 사용
#    type 검사(자료형이 지정되어 있지 않다)
# 3) 변수는 이름을 가지고 있다.
# 4) 변수는 다른 값을 저장할 수 있다.(값 변경 가능)
# 5) 변수는 선언이 필요없다.

# 자바 : int x
#       x = 100.0(오류)



x = 10
print(x)
id(x) # 변수가 가리키는 값의 주소
type(x) # 변수가 가리키는 값의 형식

y = 'hello'
print(y)
y = 'haha'
print(y)
y = 100
print(y)
y = 10.5

y = {10, 30, 40}
id(y)
type(y)

z = y

# 변수 이름
# 1) 대소문자 구분: c 언어 기반
    X x
# 2) 영문자,
# snake : std_name
# camel: stdName
# 4) 예약어는 변수명을 사용할 수 없다.


# 변수에 값 저장: 할당(assign)
# 변수 = 값
a = 100

# 변수1, 변수2, 변수3 = 값1., 값2, 값3
a, b, c = 1, 2, 3

# 변수1 = 변수2= 변수3 = 값1
a = b = c = 100

# 변수값 교환(swop)
a, b = b, a

#변수 삭제: del 변수명
del z


name = '김연우'
age = 25
print("제이름은" + "이고" + name + "나이는" + str(age) + "입니다")

name = "성명: 홍길동"
no = "학번: 2016001"
year = "학년: 4"
grade = "학점: A"
average = "평균: 93.5"
print(f'{name} {no} {year}')


#포맷 코드 사용
name = '김연우'
age = 25
print('나이: %d살' % age)
print('이름: %s' % name )










