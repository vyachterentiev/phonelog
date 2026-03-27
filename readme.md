Установка 

Устанавливаем через pip 
pip install django 

Создаем проект : 
django-admin startproject mysite djangotutorial

manage.py - терминал утилита для управления проектом (https://docs.djangoproject.com/en/6.0/ref/django-admin/). В частности "python manage.py runserver". 

Фундамент

urls.py - адреса страниц. ДЛя переменных адресов используется "/<int:i>", "<str:name>". При этом переменная передается во вьюшку, ее нужно принимать в качестве аргумента 

from django.urls import path
from . import views
urlpatterns = [
    path("<int:id>/", views.person, name="person"),
]

views.py - сами собственно страницы. Каждая страница задается как функция. Не забыть импортировать их в urls.py. Функция всегда принимает request и переданную переменную из пути если такая есть 

from django.http import HttpResponse
def number(request, id):
    return HttpResponse(f"Page number : {id}")

Приложения (apps)
Django поддерживает модульную систему приложений. Один проект может использовать несколько приложений, которые можно переносить. Для создания нового приложения : 

python manage.py startapp polls

Для подключения приложения указываем путь к его настройкам в файлt apps.py : polls.apps.PollsConfig

Базы данных 
Для автоматической настройки базы данных : 
python manage.py migrate 

Модели 
В качестве единого источника истины используеются модели - классы в models.py. Каждый класс - подкласс django.Model. Каждый параметр - поле в базе данных или правило, контрейнт, ключ и тд 
