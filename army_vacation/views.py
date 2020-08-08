from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Vacation
from .forms import VacationForm
from datetime import date

# Create your views here.


def main_menu(request):
    return render(request, 'army_vacation/main.html')


def apply_vacation(request):
    if request.method == "POST":
        form = VacationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
        else:
            print('fail')
    else:
        form = VacationForm()
    return render(request, 'army_vacation/apply_vacation.html', {'form': form})


def login(request):
    return render(request, 'army_vacation/login.html')


def questionaire(request):
    return render(request, 'army_vacation/questionaire.html')


def handbook(request):
    return render(request, 'army_vacation/handbook.html')


def food(request, month_date):
    foods = ['김치', '쌀밥', '소고기무국', '콩나물무침']
    return render(request, 'army_vacation/food.html', {'today_food': foods})


def vacation_list(request):
    vacations = Vacation.objects.filter(start_date__lte=timezone.now()).order_by('-start_date')
    return render(request, 'army_vacation/vacation_list.html', {'vacations': vacations})

