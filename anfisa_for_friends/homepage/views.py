from django.shortcuts import render
from django.db.models import Q

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    # Для переноса длинной строки замыкаем её в скобки.
    # Будьте внимательны.
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
        ).filter(
            Q(is_published=True)
            & Q(is_on_main=True)
            | Q(title__contains='пломбир')
            & Q(is_published=True)
        )
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)


'''
    # Запрос:
    # ice_cream_list = IceCream.objects.all()
    # Возьмём нужное. А ненужное не возьмём:
    ice_cream_list = IceCream.objects.values(
        # Заключаем вызов методов в скобки
        # (это стандартный способ переноса длинных строк в Python);
        # каждый вызов пишем с новой строки, так проще читать код:
        'id', 'title', 'description'
        # Верни только те объекты, у которых в поле is_on_main указано True:
        ).filter(
            is_on_main=True
            # Исключи те объекты, у которых is_published=False:
        ).exclude(is_published=False)
    # Полученный из БД QuerySet передаём в словарь контекста:
'''
