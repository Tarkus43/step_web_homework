from django.urls import path
from ..views import topics,topics_articles,topics_articles_subscribe,topics_articles_unsubscribe

urlpatterns = [
    path('', topics, name='topics'),
    path('<int:topic_id>/', topics_articles, name='topics_articles'),
    path('<int:topic_id>/subscribe/', topics_articles_subscribe, name='topics_articles_subscribe'),
    path('<int:topic_id>/unsubscribe/', topics_articles_unsubscribe, name='topics_articles_unsubscribe'),
]