######################################################
# Section 01
# 제어문 if 실습
######################################################

# 기본 형식
# if 기본 형태 - 참(또는 거짓)인 경우
if True:
    print('True')

if False:
    print('False')

# if 기본 형태2 - else
# if True:
if False:
    print('True')
else:
    print('False')

# 관계 연산자
# >, >=, <, <=, ==, !=
# int 변수 a, b
a = 30
b = 50
if a < b:
    print('A < B')
a = 30
b = 15
if 30 < 15:
    print('A < B')

# == 양 변이 같을 때 참.
if 20 == 20:
    print('20 == 20')

# != 양 변이 다를 때 참.
if 20 != 20:
    print('20 != 20')
    print('if는 들여쓰기 기준으로 실행1')
    print('if는 들여쓰기 기준으로 실행2')
    print('if는 들여쓰기 기준으로 실행3')
print('end if.')

# > 왼쪽이 클때 참.
if 20 > 20:
    print('20 > 20')

# >= 왼쪽이 크거나 같을 때 참.
if 20 >= 20:
    print('20 >= 20')

# < 오른쪽이 클 때 참.
if 20 < 20:
    print('20 < 20')

# <= 오른쪽이 크거나 같을 때 참.
if 20 <= 20:
    print('20 <= 20')

# 참 거짓 예시
# 참: "값" or '값', [값], (값), {값}, 1
# 거짓: "", [], (), {}, 0, None

# 조건이 거짓인 경우 - movie_type = ''
movie_type = ''
if movie_type:
    print(movie_type, '입력하셨습니다.')
else:
    print('장르를 입력해주세요.')

# 조건이 참인 경우 - movie_type = '코미디'
movie_type = '코미디'
if movie_type:
    print(movie_type, '입력하셨습니다.')
else:
    print('장르를 입력해주세요.')

print('A', 'B', 'C', end='\n\n\n')
print('A', 'B', 'C')

# 논리 연산자 and, or, not
score = 88
print(80 < score and score < 90)

score = 88
print(80 < 88 or 90 < 88)
#        참        거짓
# if 80 < 88 or 90 < 88: ...

print(not True)

# 산술, 관계, 논리 우선순위 - 산술 > 관계 > 논리 순서 적용
print((80 < 88) or (90 < 88))

# 점수와 학점
score = 91
if 90 < score:
    print('A')
elif 80 < score:  # 80 < score and score < 90
    print('B')
else:
    print('F')

# 관리자 사이트 권한
is_active = True
is_admin = True
if is_active and is_admin:
    print('로그인 처리')
else:
    print('로그인 실패')

# 중첩 조건문
# 신체검사 키, 몸무게
age = 20
kg = 30
if 19 < age:
    if 40 < kg:
        print('지원 가능')
    else:
        print('몸무게 미달, 지원 불가.')
else:
    print('나이 미달, 지원 불가.')

# in, not in
movie_type = ['코미디', '액션', '드라마']
print('코미디' in movie_type)
print('스릴러' not in movie_type)


# print 사용 방법 - 추천
# name = 'korea'
# display_string = name + '님 안녕하세요.'
# display_string = f'{name}님 안녕하세요.222'
# print(f'{name}님 안녕하세요.') # 1
# print(name, '님 안녕하세요.') # 2
# print(name + '님 안녕하세요.') # 3
# print(display_string)