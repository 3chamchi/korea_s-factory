######################################################
# Section 02
# 파이썬 데이터 타입 퀴즈
######################################################

################################
# A 데이터 타입
################################
# A-1. '010-0000-2222'의 값을 변수명 phone로 저장
phone = '010-0000-2222'

# A-2. 변수 phone에서 뒷 4자리 번호 출력
print(phone[9:])
print(phone[-4:])

# A-3. 영화의 장르 코미디, 액션, 로맨스를 리스트 변수명 movie_type로 저장
movie_type = ['코미디', '액션', '로맨스']

# A-4. movie_type의 변수에 '스릴러' 장르를 추가
movie_type += ['스릴러']
movie_type = movie_type + ['스릴러']
print(movie_type)

# movie_type.append('스릴러')
# print(movie_type)

# A-5. number 변수에 '880616-1413429' 값을 저장
number = '880616-1413429'

# A-6. number 변수에서 성별을 출력
# * 주민번호 첫 번째 값이 1인 경우 남성, 2인 경우 여성
print(number[7])

# A-8. age 변수에 문자열 '36'을 저장하고 int형으로 형변환
age = '36'
print(age, type(age))
age = int(age)
print(age, type(age))

# A-9. 자판기를 만든다는 과정을 두고 자판기에는 콜라 1500원 사이다 1500원 물 800원을 products 변수에 저장하시오.
products = {
    '콜라': 1500,
    '사이다': 1500,
    '물': 800,
}
print(products['콜라'])
print(products)

# A-10. application 변수에 리스트 형태의 1,2,3,4,5,1,2,3,4,5 값을 저장
application = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(application, type(application))

# A-11. application 변수를 set() 데이터 타입으로 형변환
application = set(application)
print(application, type(application))

################################
# B 연산자
################################
# B-1. 홍길동 38살, 홍길순 42살, 홍삼 10살이 있다 나이의 평균과 합을 출력하시오.
age_average = (38 + 42 + 10) / 3
print(age_average)

age_list = [38, 42, 10, ]
age_average = sum(age_list) / 3
print(age_average)

age_average = sum(age_list) / len(age_list)
print(age_average)

# B-2. 자신의 출생 년도를 입력 시 홀수 인지 짝수 인지 구분하는 기능을 구현하시오
# # * 예) 2000의 경우 0 출력, 2001의 경우 1 출력
year = 2022
print(year % 2)

# B-3. 임의의 원화를 입력 시 1000원, 500원, 100원과 잔돈을 계산하는 기능을 구현하시오
krw = 15200
krw = int(input('돈을 넣어주세요: '))

krw1000 = krw // 1000
_krw1000 = krw % 1000

krw500 = _krw1000 // 500
_krw500 = _krw1000 % 500

krw100 = _krw500 // 100
_krw100 = _krw500 % 100

print('krw :', krw)
print('krw1000 :', krw1000)
print('krw500 :', krw500)
print('krw100 :', krw100)
