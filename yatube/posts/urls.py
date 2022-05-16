from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('post/', views.post_list),
    path(
        'group/<slug:pk>/',
        views.group_posts
    ),
]
