from django.urls import path, include
from .views import hello_blog
from .views import post_detail

urlpatterns = [
    path('', hello_blog, name='home_blog_name'),
    path('post/<int:id>/', post_detail, name='post_detail_name'),
]