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


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request: HttpRequest) -> HttpResponse:
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
    })
