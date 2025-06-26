from django.shortcuts import render

# Create your views here.
def app_hello(request):
    return render(request, 'app_hello.html', {})