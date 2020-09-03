from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from datetime import date, timedelta
from django.conf import settings
# Create your views here.
from django.db.models import Q

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



def questionaire(request):
    return render(request, 'army_vacation/questionaire.html')


def handbook(request):
    return render(request, 'army_vacation/handbook.html')


def food(request, id=0):
    foods = get_object_or_404(Menu, date = (timezone.now()+timezone.timedelta(days=id)))
    n_food = int(id)+1
    return render(request, 'army_vacation/food.html', {'food': foods, 'n_day':n_food})


def vacation_list(request):
    vacations = Vacation.objects.filter(start_date__lte=timezone.now()).order_by('-start_date')
    return render(request, 'army_vacation/vacation_list.html', {'vacations': vacations})


def night_worker(request, name=''):
    if name == '':
        startdate = date.today()
        enddate = startdate + timedelta(days=6)
        workers = NightWorker.objects.filter(date__range=[startdate, enddate]).order_by('date')
    else:
        workers = NightWorker.objects.filter(
            Q(soldier1=name) | Q(soldier2=name)| Q(soldier3=name)| Q(soldier4=name)| Q(soldier5=name)).order_by('date')
    days = []
    for worker in workers:
        days.append(str(worker.date)[5:7]+'월'+str(worker.date)[8:]+'일')
    return render(request, 'army_vacation/worker.html', {'days' : days, 'workers' : workers})