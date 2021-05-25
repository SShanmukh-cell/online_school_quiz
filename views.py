

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import InputForm

# Create your views here.


def home_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "index.html", context)
def quiz_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "start.html", context)

