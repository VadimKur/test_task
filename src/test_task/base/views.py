from django.shortcuts import render
from .forms import MessageForm


# Create your views here.

def home(request):
    form = MessageForm()
    context = {'form': form}

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'base/home.html', context)
