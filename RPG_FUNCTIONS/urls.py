from django.urls import path
from .views import GamePostList, GamePostCreate, GamePostDetail, GamePostUpdate

# Импортируем созданное нами представление

urlpatterns = [
    path('All_Posts', GamePostList.as_view(), name = 'All_Posts'),
    path('All_Posts/add_post', GamePostCreate.as_view()),
    path('All_Posts/detail/<int:pk>', GamePostDetail.as_view()),
    path('All_Posts/update/<int:pk>', GamePostUpdate.as_view()),
]
