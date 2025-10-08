from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'game/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'game/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

from .models import PlayerProfile
from .kate import Game

@login_required
def home_view(request):
    player_profile = request.user.playerprofile
    game = Game(player_profile)
    messages = []

    if request.method == 'POST':
        action = request.POST.get('action')
        if action:
            messages = game.game_loop_turn(action)

    context = {
        'player_profile': player_profile,
        'messages': messages,
    }
    return render(request, 'game/home.html', context)

def user_agreement_view(request):
    return render(request, 'game/user_agreement.html')
