from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def post_list(request):
    return HttpResponse('Список постов')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, pk):
    return HttpResponse(f'Пост номер {pk}')
