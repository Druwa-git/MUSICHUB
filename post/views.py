from django.shortcuts import get_object_or_404, render, redirect
from .models import Record, Comment
from .forms import RecordForm, CommentForm
from django.conf import settings
import os

def handle_uploaded_file(f, name):
    with open(settings.MEDIA_URL+"musics/"+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def index(request):
    latest_record_list = Record.objects.order_by('-published_date')[:5]
    context = {'latest_record_list':  latest_record_list}
    return render(request, 'post/index.html', context)

# Create your views here.

def get_object(request, pk):
    return get_object_or_404(Record, pk=pk)

def detail(request, pk):
    record = get_object(request, pk=pk)
    latest_comment_list = Comment.objects.filter(record=pk).order_by('-published_date')
    context = {
        'record': record,
        'latest_comment_list': latest_comment_list
    }
    return render(request, 'post/detail.html', context)

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
