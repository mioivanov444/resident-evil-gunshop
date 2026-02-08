from django.shortcuts import render, get_object_or_404, redirect
from .models import Gun
from reviews.models import Review
from reviews.forms import ReviewForm

def gun_list(request):
    guns = Gun.objects.all()
    return render(request, 'guns/gun_list.html', {'guns': guns})

def gun_detail(request, slug):
    gun = get_object_or_404(Gun, slug=slug)
    reviews = gun.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.gun = gun
            review.save()
            return redirect('gun_detail', slug=gun.slug)
    else:
        form = ReviewForm()

    context = {
        'gun': gun,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'guns/gun_detail.html', context)
