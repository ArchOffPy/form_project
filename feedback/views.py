from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        if len(name) == 0:
            return render(request, 'feedback/feedback.html', context={'error_name': True})
        return HttpResponseRedirect('/done')
    return render(request, 'feedback/feedback.html', context={'error_name': False})


def done(request):
    return render(request, 'feedback/done.html')


