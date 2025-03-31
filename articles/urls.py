from django.urls import path
from .views import articles_list
from .views import articles_by_author

urlpatterns = [
    path('', articles_list),
    path('author/<str:author_name>/', articles_by_author),
]