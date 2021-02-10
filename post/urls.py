from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('record/create/', views.record_create, name='record_create'),
    path('record/modify/<int:pk>', views.record_modify, name='record_modify'),
    path('record/remove/<int:pk>', views.record_remove, name='record_remove'),
    path('comment/create/<int:pk>', views.comment_create, name='comment_create'),
    path('comment/modify/<int:record_pk>/<int:comment_pk>', views.comment_modify, name='comment_modify'),
    path('comment/remove/<int:record_pk>/<int:comment_pk>', views.comment_remove, name='comment_remove'),
]
