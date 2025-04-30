from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        return HttpResponseRedirect('/done')
    return render(request, 'feedback/feedback.html')


def done(request):
    return render(request, 'feedback/done.html')


