from django.db.models import Q
from django.shortcuts import render, get_object_or_404 , redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from .forms import CommentForm , PostForm
from .models import Post
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

User = get_user_model()

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


    #search function
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains= query) |
            Q(overview__icontains= query)
        ).distinct()

    featured = Post.objects.filter(featured = True)
    most_recent = Post.objects.order_by('-timestamp')[:8]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 8)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    
    try:
        paginated_queryset = paginator.page(page)
    
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    
    context = {
        'pag_queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'queryset': queryset,
        'featured': featured,
        'post_list':post_list
    }

    return render(request , 'blogs/blogs.html', context)


def post(request, slug):

    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid:
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(post)
            
    context = {
        'post' : post,
        'form' : form
    }

    return render(request, 'blogs/blogs_detail.html', context)

# def post_create(request):
#     form = PostForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid:
#             post_form = form.save(commit=False)
#             post_form.author = request.user
#             post_form.save()
            
            
#             return redirect(reverse('post_detail', kwargs={
#             'slug': form.instance.slug
#     }))

#     context = {
#         'form': form
#     }
    

#     return render(request, 'blogs/post_create.html', context)
# @login_required
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogs/post_create.html'

    def form_valid(self, form ,*args, **kwargs):
        post_form = form.save(commit=False)

        author = User.objects.get(username = self.request.user)
        post_form.author = author
        post_form.save()
        return super().form_valid(form, *args,**kwargs)
