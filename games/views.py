from django.shortcuts import render

# Create your views here.
def snake_game(request):
    return render(request, 'games/snake_game.html')