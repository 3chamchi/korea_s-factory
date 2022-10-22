from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo_views(reqeust):
    return HttpResponse()


def html_views(reqeust):
    return render(reqeust, 'htmltest.html')
    # demo/templates
