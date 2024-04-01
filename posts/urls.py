from django.urls import path
from posts.views import postDetail, postList



urlpatterns = [
    path('', postList.as_view(), name='post_list'),
    path('<int:pk>/', postDetail.as_view(), name='post_detail'),
]