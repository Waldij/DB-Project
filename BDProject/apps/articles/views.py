from django.shortcuts import render
from .models import Article, Comment, Photo
from .forms import SimpleAddPhotoForm
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import  reverse
from PIL import Image

def index(request):

    latest_article_list = Article.objects.order_by('-pub_date')[:5]

    return render(request, 'articles/list.html', {'latest_article_list': latest_article_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена")

    latest_comments_list = a.comment_set.order_by('-id')[:30]

    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list,})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)))

def add_simple_photo(request):
    form = SimpleAddPhotoForm()
    if request.method == 'POST':
        form =SimpleAddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            form.save(commit=True)
            return HttpResponse('image upload success')
        else:
            print(form.errors)
        return render(request, 'articles/add_simple_photo.html', {'form': form})