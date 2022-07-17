from django.shortcuts import get_object_or_404, render, redirect
from .models import MainContent


def index(request):
    content_list = MainContent.objects.all()
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)


def detail(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)
    context = {'content_list': content_list}
    return render(request, 'mysite/content_detail.html', context)


def collection(request):
    content_list = MainContent.objects.all()
    context = {'content_list': content_list}
    return render(request, 'mysite/collection.html', context)


def additem(request):
    MainContent.objects.create(
        title=request.POST['title'],
        content=request.POST['content'],
    )
    return redirect('collection')



