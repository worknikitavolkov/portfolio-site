from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name = 'blog'),
    path('<int:post_id>/', views.detail, name = 'detail'),
]
