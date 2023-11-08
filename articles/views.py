from django.shortcuts import render
from .forms import ArticleForm, CommentForm
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
    form = CommentForm()

    context = {
        'article':article,
        'form': form,
    }

    return render(request, 'detail.html', context)


def comment_create(request, article_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = article

        comment.user_id = request.user.id
        comment.article_id = article_id
        
        comment.save()

        return redirect('articles:detail', id=article.id)