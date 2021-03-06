from django.urls import path
from .views import base_views, record_views, comment_views

app_name = 'post'
urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:pk>/', base_views.detail, name='detail'),
    path('record/create/', record_views.record_create, name='record_create'),
    path('record/modify/<int:pk>', record_views.record_modify, name='record_modify'),
    path('record/remove/<int:pk>', record_views.record_remove, name='record_remove'),
    path('record/like/<int:pk>', record_views.record_like, name='record_like'),
    path('record/dislike/<int:pk>', record_views.record_dislike, name='record_dislike'),
    path('comment/create/<int:pk>', comment_views.comment_create, name='comment_create'),
    path('comment/modify/<int:record_pk>/<int:comment_pk>', comment_views.comment_modify, name='comment_modify'),
    path('comment/remove/<int:record_pk>/<int:comment_pk>', comment_views.comment_remove, name='comment_remove'),
    path('comment/like/<int:record_pk>/<int:comment_pk>', comment_views.comment_like, name='comment_like'),
    path('comment/dislike/<int:record_pk>/<int:comment_pk>', comment_views.comment_dislike, name='comment_dislike'),
]
