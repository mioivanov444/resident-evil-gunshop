from django.shortcuts import render, get_object_or_404, redirect
from .models import Gun, Category
from reviews.models import Review
from reviews.forms import ReviewForm
from django.db.models import Avg
import math
from .forms import GunForm
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q

def gun_list(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort', 'name')
    order = request.GET.get('order', 'asc')

    guns = Gun.objects.all()

    #search filter
    if query:
        guns = guns.filter(
            Q(name__icontains=query) |
            Q(game__icontains=query)
        )

    # sorting
    if sort_by in ['name', 'game']:
        if order == 'desc':
            sort_by = f'-{sort_by}'
        guns = guns.order_by(sort_by)

    return render(request, 'guns/gun_list.html', {
        'guns': guns,
        'query': query,
        'sort_by': sort_by.lstrip('-'),
        'order': order,
    })

def gun_detail(request, slug):
    gun = get_object_or_404(Gun, slug=slug)
    reviews = gun.reviews.all().order_by('-created_at')

    #Average rating
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    average_rating_int = math.floor(average_rating)

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
        'average_rating': average_rating,
        'average_rating_int': average_rating_int,
    }
    return render(request, 'guns/gun_detail.html', context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'guns/category_list.html', {
        'categories': categories
    })



def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    guns = category.guns.all()
    return render(request, 'guns/category_detail.html', {
        'category': category,
        'guns': guns
    })

@staff_member_required
def gun_create(request):
    if request.method == 'POST':
        form = GunForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gun_list')
    else:
        form = GunForm()
    return render(request, 'guns/gun_form.html', {'form': form, 'title': 'Add New Gun'})


@staff_member_required
def gun_update(request, slug):
    gun = get_object_or_404(Gun, slug=slug)
    if request.method == 'POST':
        form = GunForm(request.POST, request.FILES, instance=gun)
        if form.is_valid():
            form.save()
            return redirect('gun_detail', slug=gun.slug)
    else:
        form = GunForm(instance=gun)
    return render(request, 'guns/gun_form.html', {'form': form, 'title': f'Edit {gun.name}'})
@staff_member_required
def gun_delete(request, slug):
    gun = get_object_or_404(Gun, slug=slug)
    if request.method == 'POST':
        gun.delete()
        return redirect('gun_list')
    return render(request, 'guns/gun_confirm_delete.html', {'gun': gun})