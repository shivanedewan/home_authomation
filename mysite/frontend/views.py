from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from api.models import Board, Pin

def get_common(requests):

    return{
        'rooms':Board.objects.all()
    }

def home_view(requests):
    if not requests.user.is_authenticated:
        return redirect('login')
    context = get_common(requests)

    return render(requests, 'frontend/home.html', context)

def room_view(requests, pk):
    if not requests.user.is_authenticated:
        return redirect('login')
    context                 = get_common(requests)
    context['Room']         = get_object_or_404(Board, id=pk)
    context['appliances']   = Pin.objects.filter(board__id=pk).order_by('pin_no')
    print(context['appliances'])
    return render(requests, 'frontend/room.html', context)


def login_view(requests):
    if requests.user.is_authenticated:
        return redirect('login')

    if requests.method == 'POST':
        form = AuthenticationForm(request=requests, data=requests.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(requests, user)
                messages.info(requests, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(requests, "Invalid username or password.")
        else:
            messages.error(requests, "Invalid username or password.")
    form = AuthenticationForm()

    return render(requests, 'frontend/login.html',{"form":form})


def logout_view(requests):
    logout(requests)
    return redirect('login')

def addPin_view(requests, pk):
    data = requests.POST
    pin = Pin(  name = data.get('applianceName'),
                board = Board.objects.get(id=pk),
                pin_no = data.get('appliancePin'),
    )
    pin.save()

    return redirect('../') 

def addBoard_view(requests):
    Board(name=requests.POST.get('roomName')).save()
    return redirect('../') 

