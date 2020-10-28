#Django
from django.contrib import sessions
from django.shortcuts import render
# from django.http import render

def listado(request):
    context = {
        'name': request.user,
    }
    return render(request, 'index.html', context)
