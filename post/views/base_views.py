from django.shortcuts import get_object_or_404, render
from ..models import Record, Comment
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def handle_uploaded_file(f, name):
    with open(settings.MEDIA_URL+"musics/"+name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def get_object(request, pk):
    return get_object_or_404(Record, pk=pk)

def get_comment(request, pk):
    return get_object_or_404(Comment, pk=pk)

def index(request):
    page = request.GET.get('page', '1')
    latest_record_list = Record.objects.order_by('-published_date')[:3]
    all_record_list = Record.objects.order_by('-published_date')
    paginator = Paginator(all_record_list, 10)
    page_obj = paginator.get_page(page)
    context = {
        'latest_record_list':  latest_record_list,
        'all_record_list': page_obj
    }
    return render(request, 'post/index.html', context)

@login_required(login_url='common:login')
def detail(request, pk):
    record = get_object(request, pk=pk)
    latest_comment_list = Comment.objects.filter(record=pk).order_by('-published_date')
    context = {
        'record': record,
        'latest_comment_list': latest_comment_list
    }
    return render(request, 'post/detail.html', context)
