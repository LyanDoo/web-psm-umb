from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('articles',views.articles_page,name='articles-page'),
    path('add-article',views.add_article,name='add-article-form'),
    path('edit-article/<int:article_id>',views.edit_article,name='edit-article-form'),
    path('article/<int:article_id>',views.article_detail,name="article-detail")
]
