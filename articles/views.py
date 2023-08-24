from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article': article
    }

    return render(request, 'detail.html', context)

def create(request):
    # create 기능
    # 사용자가 입력한 데이터를 DB에 저장
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
        else:
            # form = ArticleForm()

            context = {
                'form': form
            }

            return render(request, 'create.html', context)

    # new에 해당하는 기능
    # 사용자가 데이터를 입력할 수 있도록 빈 종이를 리턴
    else:
        form = ArticleForm()

        context = {
            'form': form,
        }

        return render(request, 'create.html', context)
    