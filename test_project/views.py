from django.shortcuts import render


def home(request):
    return render(request, 'test_project/home.html', locals())


def test(request, message, name):

    return render(request, 'test_project/test_page.html', locals())
