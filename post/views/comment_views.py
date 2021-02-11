from django.shortcuts import render, redirect
from ..models import Record, Comment
from ..forms import CommentForm
from .base_views import get_object, get_comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

@login_required(login_url='common:login')
def comment_create(request, pk):
    record = get_object(request, pk=pk)
    #record.comments.create(author=request.user, content=request.POST.get('content'))
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)#save just temporary
            comment.author = request.user
            comment.record = record
            comment.save()
            return redirect('post:detail', pk=pk)
    else:
        form = CommentForm()
    #Record.objects.create(artist=request.user, song_title=request.POST.get('song_title'),  song_intro=request.POST.get('song_intro'))
    form = {'record': record, 'form': form }
    return render(request, 'post/detail.html', form)

@login_required(login_url='common:login')
def comment_modify(request, record_pk, comment_pk):
    record = get_object(request, pk=record_pk)
    comment = get_comment(request, pk=comment_pk)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('post:detail', pk=record_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)#save just temporary
            comment.author = request.user
            comment.record = record
            comment.edited_date = timezone.now()
            comment.save()
            return redirect('post:detail', pk=record_pk)
    else:
        form = CommentForm(instance=comment)
    form = {'record': record, 'form': form}
    return render(request, 'post/comment_edit.html', form)

@login_required(login_url='common:login')
def comment_remove(request, record_pk, comment_pk):
    record = get_object(request, pk=record_pk)
    comment = get_comment(request, pk=comment_pk)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('post:detail', pk=record_pk)
    comment.delete()
    return redirect('post:detail', pk=record_pk)

@login_required(login_url='common:login')
def comment_like(request, record_pk, comment_pk):
    record = get_object(request, pk=record_pk)
    comment =get_comment(request, pk=comment_pk)
    if request.user == comment.author:
        messages.error(request, '본인이 추천할 순 없어요~')
    else:
        comment.like.add(request.user)
    return redirect('post:detail', pk=record_pk)

@login_required(login_url='common:login')
def comment_dislike(request, record_pk, comment_pk):
    record = get_object(request, pk=record_pk)
    comment =get_comment(request, pk=comment_pk)
    if request.user == comment.author:
        messages.error(request, '본인이 비추천할 순 없어요~')
    else:
        comment.dislike.add(request.user)
    return redirect('post:detail', pk=record_pk)
