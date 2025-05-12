from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm


def index(request):

    if request.method == 'POST':
         # создаем экземпляр класса FeedbackForm, помещаем в него запрос
        form = FeedbackForm(request.POST)
        # таким образом проверяем, пустая ли форма. И если не пустая то обрабатываем
        if form.is_valid():
            # просто выведем в консоль
            print(form.cleaned_data)
            # возвращаем успешный шаблон
            return HttpResponseRedirect('/done')
    # иначе снова создаем пустую форму и отображаем ее в шаблоне
    form = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request):
    return render(request, 'feedback/done.html')


