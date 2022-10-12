######################################################
# Section 01
# 파이썬 분기 처리 퀴즈
# 제어문 if, 반복문 for
######################################################

# Section03
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈

## if
# 1. 학생의 점수 입력 시 학점 계산 기능을 구현하시오.
# A : 90 이상
# B : 80 이상 90 미만
# C : 70 이상 80 미만
# D : 60 이상 70 미만
# F : 60 미만
score = 90
# score = int(input('점수를 입력해주세요 : '))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

# 2. 업다운 게임을 구현하시오.
# 기본
# 업 다운 범위 1~50
# 입력한 값 보다 높은 경우 "업" 출력
# 입력한 값 보다 낮은 경우 "다운" 출력
# 맞힌 경우 "정답" 출력
# 심화
# 정답 숫자를 입력 받아서 진행, "0"을 입력 받은 경우 종료
# 참고 기능 : input(), exit(), random()
import random

random_number = random.randrange(50)
print(f'random_number : {random_number}')

print('[업다운 게임] 0~50까지 숫자 중 입력해주세요.')

game_count = 0
while True:
    input_number = int(input('숫자를 입력해주세요 : '))
    game_count = game_count + 1

    if input_number == 0:
        break

    if random_number == input_number:
        print('정답')
        break
    elif random_number > input_number:
        print('업')
    else:
        print('다운')

    print(f'Game count : {game_count}')

# 3. 자판기 소프트웨어를 구현하시오.
# 자판기 상품 콜라 1500원 사이다 1500원 물 800원
# 자판기 기능
# 1. 현금 입력(input() 활용)
# 2. 상품 선택
# 3. 상품, 거스름돈 출력(print() 활용)
products = {
    1: {'NAME': '콜라', 'PRICE': 1500, },
    2: {'NAME': '사이다', 'PRICE': 1500, },
    3: {'NAME': '물', 'PRICE': 800, },
}

print('==================')
print('상품 목록')
print('1. 콜라 1500원')
print('2. 사이다 1500원')
print('3. 물 800원')
print('==================')
# for key in products:
#     print(f'{key}. {products[key]["NAME"]} {products[key]["PRICE"]}원')

money = int(input('자판이 현금을 투입해주세요 : '))
choice = int(input('구매할 상품의 번호를 입력해주세요 : '))

if money < products[choice]['PRICE']:
    print('현금이 부족합니다.')
else:
    product_name = products[choice]["NAME"]
    change = money - products[choice]["PRICE"]
    print(f'{product_name} 상품 출력. 잔돈 {change}')
