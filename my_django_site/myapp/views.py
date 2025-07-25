from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def main_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('This is main page!')


def my_feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse('This is your main feed page!')

def article_id(request: HttpRequest, id:int) -> HttpResponse:
    return HttpResponse(f"This is article #{id}")

def article_id_delete(request: HttpRequest, id:int) -> HttpResponse:
    return HttpResponse(f"This is an after deleting page of article #{id}")

def article_id_comment(request: HttpRequest, id:int) -> HttpResponse:
    return HttpResponse(f"This is a page to write a comment to article #{id}")


