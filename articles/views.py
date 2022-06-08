from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article
from .forms import ArticleModelForm

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    # display list from newest to oldest
    queryset = Article.objects.all().order_by('-id')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    login_url = '/login/'