from django.shortcuts import render, redirect
from ..models import Record
from ..forms import RecordForm
from .base_views import get_object
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pytz import timezone


@login_required(login_url='common:login')
def record_create(request):
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)#save just temporary
            record.artist = request.user
            record.save()
            #name = record.song_file.name.split('/')[1]
            #name = os.path.basename(record.song_file.name)
            #handle_uploaded_file(request.FILES['song_file'], name)
            return redirect('post:index')
    else:
        form = RecordForm()
    #Record.objects.create(artist=request.user, song_title=request.POST.get('song_title'),  song_intro=request.POST.get('song_intro'))
    form = {'form': form }
    return render(request, 'post/record_create.html', form)

@login_required(login_url='common:login')
def record_modify(request, pk):
    record = get_object(request, pk=pk)
    if request.user != record.artist:
        messages.error(request, '수정권한이 없습니다')
        return redirect('post:detail', pk=pk)

    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            record = form.save(commit=False)#save just temporary
            record.artist = request.user
            record.edited_date = timezone.now()
            record.save()
            return redirect('post:detail', pk=pk)
    else:
        form = RecordForm(instance=record)
    form = {'form': form}
    return render(request, 'post/record_create.html', form)

@login_required(login_url='common:login')
def record_remove(request, pk):
    record = get_object(request, pk=pk)
    if request.user != record.artist:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('post:detail', pk=pk)
    record.delete()
    return redirect('post:index')

@login_required(login_url='common:login')
def record_like(request, pk):
    record = get_object(request, pk=pk)
    if request.user == record.artist:
        messages.error(request, '본인이 추천할 순 없어요~')
    else:
        record.like.add(request.user)
    return redirect('post:detail', pk=pk)

@login_required(login_url='common:login')
def record_dislike(request, pk):
    record = get_object(request, pk=pk)
    if request.user == record.artist:
        messages.error(request, '본인이 비추천할 순 없어요~')
    else:
        record.dislike.add(request.user)
    return redirect('post:detail', pk=pk)
