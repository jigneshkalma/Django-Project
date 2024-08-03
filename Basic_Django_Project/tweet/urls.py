from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('Create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/Edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/Delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register')
] 
