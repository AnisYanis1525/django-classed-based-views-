from django.contrib import admin
from django.urls import path

from . import views
app_name = "post"
urlpatterns = [
    path('', views.PostList.as_view(), name='postlist' ),
    path('<int:pk>/', views.PostDetail.as_view(),name= "post_detail"),
]
