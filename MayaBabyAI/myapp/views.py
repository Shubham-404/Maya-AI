from django.shortcuts import render

# Create your views here.

# myapp/views.py

def index(request):
    return render(request, 'index.html')

#added manually