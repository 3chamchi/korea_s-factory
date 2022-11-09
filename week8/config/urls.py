from django.contrib import admin
from django.urls import path

from posts.views import new, create, list, detail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('new/', new, name='new'),
    path('create/', create, name='create'),

    path('', list, name='list'),
    path('<int:id>/', detail, name='detail')
]
