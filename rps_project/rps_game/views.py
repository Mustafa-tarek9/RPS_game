from django.shortcuts import render

def rock_paper_scissors(request):
    return render(request, 'rps_game/game.html')