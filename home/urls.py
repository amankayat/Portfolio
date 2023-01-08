from django.urls import path
from . import views


urlpatterns = [
     
    path('',views.home,name = "home"),
    path('blog/',views.blogpage,name="blog_page"),
    path('blogdetails/<int:pk>',views.blogdetails,name="blogdetails")
]
