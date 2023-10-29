from django.http import HttpResponse
from django.shortcuts import redirect, render
from listings.models import Category

# Create your views here.


def index(request):
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request, 'index.html', {'cat': category})
    if request.method == 'POST':
        return redirect('all_listing')
