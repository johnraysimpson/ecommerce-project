from django.shortcuts import render

# Create your views here.
def index(request):
    """render a homepage named index.html"""
    return render(request, 'index.html')
