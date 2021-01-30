from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('record/create/', views.record_create, name='record_create'),
    path('comment/create/<int:pk>', views.comment_create, name='comment_create'),
]
