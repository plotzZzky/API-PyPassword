from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# Errors

def error_400(request, exception=None):
    return render(request, 'errors/400.html', {})


def error_403(request, exception=None):
    return render(request, 'errors/403.html', {})


def error_404(request, exception):
    return render(request, 'errors/404.html', {})


def error_405(request):
    return render(request, 'errors/405.html', {})


def error_500(request, exception=None):
    return render(request, 'errors/500.html', {})

