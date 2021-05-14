from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models


# Create your views here.
def index(request):
    user = models.User.objects.get(id=request.user.id)
    if user == None:
        return redirect('login')

    maincycle = models.MainCycle.objects.get(user=request.user)

    return render(request, 'index.html', {'maincycle': maincycle})


@api_view(['GET'])
def call_click(request):
    maincycle = models.MainCycle.objects.first()
    maincycle.click()
    maincycle.save()
    
    return Response(maincycle.coins_count)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            main_cycle = models.MainCycle()
            main_cycle.user = user
            main_cycle.save()

            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})

        
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})