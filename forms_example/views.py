from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.


def review_input(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})


