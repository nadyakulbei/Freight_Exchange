from django.urls import path, include
from . import views
from users import views as user_views
from .views import PostDeleteView
from .views import NewsUpdateView

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('register', user_views.register, name='register'),
    path('delete', views.delete, name='delete'),
    path('post-detail', views.post_detail, name='post-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-detail'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete')
    ]