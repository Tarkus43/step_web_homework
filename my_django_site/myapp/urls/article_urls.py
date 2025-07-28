from django.urls import path
from ..views import article_id,article_id_comment,article_id_delete,article_id_update

urlpatterns =[
    path('<int:article_id>/',article_id, name='article'),
    path('<int:article_id>/comment/', article_id_comment, name='article_comment'),
    path('<int:article_id>/delete/', article_id_delete, name='delete_article'),
    path('<int:article_id>/update',article_id_update, name='update_article'),
]