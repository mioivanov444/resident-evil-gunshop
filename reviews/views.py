from django.shortcuts import render, get_object_or_404, redirect
from guns.models import Gun
from .forms import ReviewForm
from .models import Review
from django.contrib.admin.views.decorators import staff_member_required

def review_create(request, gun_slug):
    gun = get_object_or_404(Gun, slug=gun_slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.gun = gun
            review.save()
            return redirect('gun_detail', slug=gun.slug)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form, 'gun': gun, 'title': f'Add Review for {gun.name}'})


@staff_member_required
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('gun_detail', slug=review.gun.slug)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', {'form': form, 'title': f'Edit Review', 'gun': review.gun})


@staff_member_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    gun = review.gun
    if request.method == 'POST':
        gun_slug = review.gun.slug
        review.delete()
        return redirect('gun_detail', slug=gun_slug)
    return render(request, 'reviews/review_confirm_delete.html', {'review': review, 'gun': gun})
