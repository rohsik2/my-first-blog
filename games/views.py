from django.shortcuts import render

# Create your views here.
def go_game(request):
    return render(request, 'games/go.html')

def game_list(request):
    return render(request, 'games/game_lists.html')