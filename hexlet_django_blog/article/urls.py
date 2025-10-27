from django.urls import path
from hexlet_django_blog.article import views
from .views import Article_home_page


urlpatterns = [
    path('', Article_home_page.as_view()),
]