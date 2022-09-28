######################################################
# Section 01
# 파이썬 데이터 타입(자료형) 실습
######################################################

# a = 3
# True
# true

'''
[파이썬 자료형]
   int : 정수
   float : 실수
   str : 문자열
   list : 리스트
   tuple : 튜플
   set : 집합
   dict : 사전
'''

'''
[연산자]
산술 연산자
   + : 더하기
   - : 빼기
   * : 곱하기
   ** : 제곱
   / : 나누기
   // : 나누기 몫
   % : 나누기 나머지

비교 연산자
   == : 값이 같다면
   != : 값이 같지 않다면
   > : 왼쪽 값이 더 크다면
   < : 오른쪽 값이 더 크다면
   >= : 왼쪽 값이 크거나 같다면
   <= : 오른쪽 값이 크거나 같다면

논리 연산자
   and : 좌우 조건문이 참(ture)인 경우
   or : 좌우 조건문 중 하나라도 참(true)인 경우
   not : 조건문 자체가 거짓인 경우

[참고 함수]

   print() : 데이터 출력
   type() : 데이터 타입 확인
   id() : 객체 고유값 확인
'''

# int : 정수
# int a = 40
a = 20
b = 40
sum = a + b
print(b)
print(a + b)
b = 'awda'  # or ""

print(9999 * 3)
age = 20
print(age - 60)
print(type(age))
# float : 실수
print('float===============')
a = 20.0
print(a)
type(a)
print(type(a))

print(a * 3)
print(type(a * 3))

# str : 문자열
# print("str============")
print('str============')
a = 'abc'
print(a)
type(a)
print(type(a))
# 인덱싱
print(a[0])
print(a[1])
print(a[2])
# 슬라이싱 abc
print(a[1:3])
phone = '010-0000-1234'
print(phone[9:13])
print('20' + '5')
print(20 + 5)

# list : 리스트
print('list============')
#    0  1  2  3  ...
a = [1, 2, 3, 4, 'a', '22', 40.0]
print(a)
print(a[3])
print(a[3:5])

# tuple : 튜플
print('tuple============')
a = (1, 2, 3, 4)
print(a)
print(a[3])
print(a[3:6])
# set : 집합

# dict : 사전
print('dict=====')
a = {'키': '값'}
a = {
    '이름': '홍길동',
    '나이': 20,
    '번호': '000-0000-0000'
}
print(a)
print(a['이름'])

# 형변환
a = [1,2,3,4]
print(type(a))
print(tuple(a))
a1 = '20'
a2 = int(a1)
print(a1)
print(a2)
print(type(a1))
print(type(a2))
