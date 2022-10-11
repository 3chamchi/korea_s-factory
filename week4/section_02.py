######################################################
# Section 02
# 반복문 while, for 실습
######################################################

# 기본 반복문 사용(while, for)
# while
while False:  # True
    print('while True')

var_input = ''
# while var_input != 'exit':
#     var_input = input('입력 값: ')
#     print(f'{var_input} 입력!')
# 입력에 따른 값 처리

# for
movie_type = ['코미디', '액션', '드라마']

for movie in movie_type:
    print(movie)

movie_type = ['코미디', '액션', '드라마']
for movie in movie_type:
    if '코미디' == movie:
        print(True)

# 1 ~ 100 합 계산
numbers = [1, 2, 3, 4, 5, 6, ]
number_sum = 0
for index in numbers:
    number_sum = number_sum + index
print(number_sum)

for index in range(100):
    print(index)
print(range(100))

for index in range(10):
    for index2 in range(10):
        print(f'{index} x {index2} = {index * index2}')

number_sum = 0
for number in range(100):
    print(number)
    number_sum = number_sum + number
print(number_sum)

print(sum(range(100)))

# for -> while
number = 0
while number < 100:
    print(number)
    number = number + 1

number_sum = 0
for number in range(100):
    print(number)
