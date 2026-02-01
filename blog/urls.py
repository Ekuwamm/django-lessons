from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog_post, name='blog-post'),
    path('search_page/',views.search_page, name="search"),
    path('blog_page/<slug:slug>/',views.blog_page, name='page'),

]
