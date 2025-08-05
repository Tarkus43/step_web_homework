from django.shortcuts import render
from django.http import HttpResponse, HttpRequest



def main_page(request: HttpRequest) -> HttpResponse:
    return  render(request, 'components/main.html', {
        
    })


def my_feed(request: HttpRequest) -> HttpResponse:
    return  render(request, 'components/feed.html', {
        
    })

def article_id(request: HttpRequest, article_id:int) -> HttpResponse:
    return HttpResponse(f"This is article #{article_id}")

def article_id_delete(request: HttpRequest, article_id:int) -> HttpResponse:
    return HttpResponse(f"This is an after deleting page of article #{article_id}")

def article_id_comment(request: HttpRequest, article_id:int) -> HttpResponse:
    return HttpResponse(f"This is a adress to write a comment to article #{article_id}")

def article_id_update(request: HttpRequest,article_id ) -> HttpResponse:
    return HttpResponse(f'This is a page to updating #{article_id} article')

def article_id_delete(request: HttpRequest,article_id ) -> HttpResponse:
    return HttpResponse(f'This is an adress to deleting #{article_id} article')

def create(request: HttpRequest ) -> HttpResponse:
    return  render(request, 'components/create.html', {
        
    })

def topics(request: HttpRequest ) -> HttpResponse:
    return  render(request, 'components/topics.html', {
        
    })

def topics_articles(request: HttpRequest,topic_id ) -> HttpResponse:
    return HttpResponse(f'This is a page with articles for #{topic_id} topic')

def topics_articles_subscribe(request: HttpRequest,topic_id ) -> HttpResponse:
    return HttpResponse(f'This is an adress for subscribing to {topic_id} topic ')

def topics_articles_unsubscribe(request: HttpRequest,topic_id ) -> HttpResponse:
    return HttpResponse(f'This is an adress for unsubscribing to {topic_id} topic ')

def profile(request: HttpRequest) -> HttpResponse:
    return  render(request, 'components/profile.html', {
        
    })

def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse('This is register page')

def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse('This is setting password page')

def login(request: HttpRequest) -> HttpResponse:
    return  render(request, 'components/login.html', {
        
    })

def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse('This is logout adress')











