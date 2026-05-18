from django.urls import path
from . import views

urlpatterns = [
    path('',           views.list_blogs,  name='list-blogs'),
    path('<int:id>/',  views.get_blog,    name='get-blog'),
    path('create/',    views.create_blog, name='create-blog'),
    path('edit/<int:id>/', views.edit_blog, name='edit-blog'),
    path('register/', views.register, name='register'),
]