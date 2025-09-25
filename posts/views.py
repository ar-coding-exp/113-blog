from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post, Status
from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        DeleteView,
        UpdateView
)

# Create your views here.
#from .models import password_validation
#CRUD -> create, read, update and delete app 
#The generic classes are ListView, CreateView, UpdateView, DeleteView and DetailView
#
# Create your views here.

#"""
#PostListView is going to retrieve all the object from the Post table in the db
#"""

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post 
    context_object_name = "post_list"
    status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=status).order_by("created_on").reverse

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class PostDraftListView(ListView):
    template_name = "posts/list.html"
    model = Post 
    context_object_name = "post_list"
    status = Status.objects.get(name="draft")
    queryset = Post.objects.filter(status=status).order_by("created_on").reverse

class PostArchiveListView(ListView):
    template_name = "posts/list.html"
    model = Post 
    context_object_name = "post_list"
    status = Status.objects.get(name="archived")
    queryset = Post.objects.filter(status=status).order_by("created_on").reverse

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post   
    context_object_name = "single_post"

    #"""
    #PostCreateView is going to allow us to create a new post and add it to the db
    #"""
class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title","subtitle","body"]

    def form_valid(self, form):
        print(form)
        form.instance.author = User.objects.filter(is_superuser=True).first()
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts')
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/edit.html'
    fields = ['title', 'subtitle', 'body']