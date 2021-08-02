from django.shortcuts import render


def login_view(request):
    context={}
    return render(request, 'login.html', context)


def register_view(request):
    context={}
    return render(request, 'register.html', context)
        