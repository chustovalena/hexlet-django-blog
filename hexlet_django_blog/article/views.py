from django.shortcuts import render
from django.http import HttpResponse
from hexlet_django_blog.views import HomePageView
# Create your views here.

class Article_home_page(HomePageView):
    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["app_name"] = "Article"
        return context
