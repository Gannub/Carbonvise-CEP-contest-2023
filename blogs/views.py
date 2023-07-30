from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post

# Create your views here.

#def index(request):
    #featured = Post.objects.filter(featured = True)
    #latest = Post.objects.order_by('-timestamp')[0:5]
    #context = {
        #'object_list': featured,
        #'latest' : latest
    #}
    #return render(request , 'blogs/blogs.html', context)

def blog(request):
    question = "what is this" 
    answer = 'Page search'
    most_recent = Post.objects.order_by('-timestamp')[:5]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    
    try:
        paginated_queryset = paginator.page(page)
    
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    
    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var

    }

    return render(request , 'blogs/blogs.html', context)


def post(request):

    return render(request)