from django.contrib import admin
from django.urls import path

from posts.views import index, new, create, list, detail, edit, update, confirm_delete, delete

urlpatterns = [
    path('admin/', admin.site.urls),

    path('new/', new, name='new'),
    path('create/', create, name='create'),

    path('', index, name='list'),
    path('<int:id>/', detail, name='detail'),

    path('<int:id>/edit/', edit, name='edit'),
    path('<int:id>/update/', update, name='update'),

    path('<int:id>/confirm-delete/', confirm_delete, name='confirm_delete'),
    path('<int:id>/delete/', delete, name='delete')
]






