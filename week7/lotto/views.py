import random

from django.http import HttpResponse
from django.shortcuts import render


def get_lotto_number(request):
    # 목표
    # 1. 로또 번호 몇개를 생성 할건지
    # 생략
    # 2. 로또 생성
    lotto_number_list = []  # list()
    for index in range(7):
        numbers = random.randrange(1, 45)
        # 중복 제거
        # if numbers not in lotto_number_list:
        # lotto_number_list.append(numbers)
        print(numbers)

        lotto_number_list.append(numbers)
    print(lotto_number_list)

    data = {
        'lotto_number_list': lotto_number_list
    }

    # 3. HTML 응답
    return render(request, 'lotto.html', data)


def lotto_numbers(request):
    # 연습
    # 1. 로또 번호 생성
    # 로또 번호 6 + 1 7자리 숫자
    # 번호 범위 1~45
    # lotto_number = random.randrange(1, 45)
    # print(lotto_number)

    lotto_number_list = []  # list()
    for index in range(7):
        numbers = random.randrange(1, 45)
        # 중복 제거
        # if numbers not in lotto_number_list:
        # lotto_number_list.append(numbers)
        print(numbers)

        lotto_number_list.append(numbers)
    print(lotto_number_list)

    # 2. 번호 TEXT 응답
    return HttpResponse(lotto_number_list)

    # 목표
    # 1. 로또 번호 몇개를 생성 할건지
    # 2. 로또 생성
    # 3. HTML 응답
    pass
