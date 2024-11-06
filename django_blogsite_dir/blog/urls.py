from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),

    # Blog Detail Url

    path('blog/detail/<pk>', views.Blog_Detail, name='blog-detail'),
]















