from django.shortcuts import render

def homepage(request):
    return render(request=request,
                  template_name='homepage.html',
                  context={})


def about(request):
    return render(request=request,
                  template_name='about.html',
                  context={})


def contact(request):
    return render(request=request,
                  template_name='contact.html',
                  context={})