"""lighthouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# views
from django.views.generic import TemplateView
from pages.views import AboutView
from articles.views import ArticleListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sw.js', (TemplateView.as_view(template_name="app/sw.js", content_type='application/javascript', )), name='sw.js'),
    path('', include("django.contrib.auth.urls")),
    path('', ArticleListView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('articles/', include('articles.urls'), name='articles'),
    path('articles/', ArticleListView.as_view(), name='articles'),
]
