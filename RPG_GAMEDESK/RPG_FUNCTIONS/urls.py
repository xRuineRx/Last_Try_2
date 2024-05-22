from django.urls import path
from .views import GamePostList, GamePostCreate

# Импортируем созданное нами представление

urlpatterns = [
    path('All_Posts', GamePostList.as_view()),
    path('All_Posts/add_post', GamePostCreate.as_view()),
]
