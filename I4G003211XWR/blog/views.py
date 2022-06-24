from django.shortcuts import render

# Create your views here.
from I4G003211XWR.blog.models import Post


def PostListView():
    model = Post
    pass


def PostCreateView():
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    pass


def PostDetailView():
    model = Post


def PostUpdateView():
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


def PostDeleteView():
    models = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
