from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ScoreForm
from .models import Score

# View to add a score
def add_score(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_scores')
    else:
        form = ScoreForm()
    return render(request, 'tracker/add_score.html', {'form': form})

# View to see all scores
def view_scores(request):
    scores = Score.objects.all().order_by('-year')
    return render(request, 'tracker/view_scores.html', {'scores': scores})

# Create your views here.
