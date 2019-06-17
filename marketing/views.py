from django.shortcuts import render
from marketing.models import News
from django.http import HttpResponseNotFound

def blog(request, blog_id) :

    blog_detail = News.objects.filter(id=blog_id)
    if not blog_detail:
        return HttpResponseNotFound('<h1>Page not found!</h1>')

    recent_blogs = News.objects.filter().exclude(id=blog_id).order_by('id')
    if not recent_blogs:
        recent_blogs = []
    NEWS_TYPE = (
        'Promotion',
        'Normal',
        'Project',
    )
    context = {
        'blog_detail': blog_detail,
        'recent_blogs': recent_blogs,
        'categories': NEWS_TYPE,
    }
    return render(request, 'blog/blog_detail.html', context)