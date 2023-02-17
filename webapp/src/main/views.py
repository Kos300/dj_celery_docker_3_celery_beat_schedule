from django.http import HttpResponse
from . import tasks


# Create your views here.

def home(request):
    # вызываем task
    # .delay() - выставить задачу
    # в очередь в асинхронном режиме
    tasks.download_a_cat.delay()
    return HttpResponse('<h1>Загружаю фото кота!!!!</h1>')

