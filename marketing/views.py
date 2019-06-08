from django.shortcuts import render

def blog(request, blog_id):
    context = {
        'blog_detail': '',
    }
    return render(request, 'blog/blog_detail.html', context)