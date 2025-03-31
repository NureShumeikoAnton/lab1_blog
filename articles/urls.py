from django.urls import path
from .views import articles_list
from .views import articles_by_author
from .views import article_detail

urlpatterns = [
    path('', articles_list, name='articles_list'),
    path('author/<str:author_name>/', articles_by_author),
    path('<int:article_id>/', article_detail, name='article_detail'),
]