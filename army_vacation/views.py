from django.shortcuts import render

# Create your views here.


def main_menu(request):
    return render(request, 'army_vacation/main.html')


def apply_vacation(request):
    return render(request, 'army_vacation/apply_vacation.html')


def login(request):
    return render(request, 'army_vacation/login.html')


def questionaire(request):
    return render(request, 'army_vacation/questionaire.html')


def handbook(request):
    return render(request, 'army_vacation/handbook.html')

