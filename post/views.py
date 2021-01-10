from django.shortcuts import get_object_or_404, render
from .models import Record

def index(request):
    latest_record_list = Record.objects.order_by('-published_date')[:5]
    context = {'latest_record_list':  latest_record_list}
    return render(request, 'post/index.html', context)

# Create your views here.

def get_object(request, pk):
    return get_object_or_404(Record, pk=pk)

def detail(request, pk):
    record = get_object(request, pk=pk)
    return render(request, 'post/detail.html', {'record': record})
