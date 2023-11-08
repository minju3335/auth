from django.shortcuts import render
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'index.html')

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valie():
            article = form.save(commit=False)
            article.user = request.user
            artcle.save()
            return redirect('article:index')
    else:
        form = ArticleForm()

    context = {
        'form':form,
    }

    return render(request, 'form.html', context)



def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article':article
    }

    return render(request, 'detail.html', context)
