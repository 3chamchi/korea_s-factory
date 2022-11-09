import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo_view(request):
    return HttpResponse('Hello world!')
    # return render(request, 'demo.html')


def lotto_view(request):
    game = request.GET.get('game')

    lotto_list = list()
    for index in range(int(game)):

        lotto_number = list()
        for index2 in range(6):
            number = random.randint(1, 45)
            lotto_number.append(number)
        lotto_list.append(lotto_number)

    print(lotto_list)

    if game:
        return render(request, 'lotto.html', {'lotto_list': lotto_list, 'game': game})
    else:
        return render(request, 'lotto.html')
