from django.shortcuts import render, get_object_or_404
from .models import Article, Notice


def article(request, article_id):
    site_article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article.html', {'article': site_article})


def notice(request, notice_id):
    site_notice = get_object_or_404(Notice, pk=notice_id)
    return render(request, 'notice.html', {'notice': site_notice})


def site_help(request):
    articles = Article.objects.all()
    context = {'articles' :articles}
    return render(request, 'help_table.html',context)


def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'notice_list.html' ,{'notices':notices})


# Create your views here.
