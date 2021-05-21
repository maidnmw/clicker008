from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from .serializers import MainCycleSerializer, BoostSerializer

# Create your views here.
def index(request):
    user = models.User.objects.get(id=request.user.id)
    if user == None:
        return redirect('login')

    maincycle = models.MainCycle.objects.get(user=request.user)
    boosts = models.Boost.objects.filter(main_cycle=maincycle)

    return render(request, 'index.html', {
        'maincycle': maincycle, 
        'boosts': boosts,
    })


@api_view(['GET'])
def call_click(request):
    maincycle = models.MainCycle.objects.get(user=request.user)
    maincycle.click()
    maincycle.save()
    
    return Response(maincycle.coins_count)


@api_view(['POST'])
def update_boost(request):
    boost_id = request.data['boost_id']
    maincycle = models.MainCycle.objects.get(user=request.user)
    
    boost = models.Boost.objects.get(id=boost_id)
    boost.update_boost()
    boost.save()
    
    return Response({
        'main_cycle': MainCycleSerializer(maincycle).data,
        'boost': BoostSerializer(boost).data,
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            main_cycle = models.MainCycle()
            main_cycle.user = user
            main_cycle.save()

            boost = models.Boost(main_cycle=main_cycle)
            boost.save()

            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})

        
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})