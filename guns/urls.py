from django.urls import path
from .views import gun_list, gun_detail, category_detail, gun_create, gun_update, gun_delete, category_create, category_list, category_delete, category_update


urlpatterns = [
    path('', gun_list, name='gun_list'),
    path('add/', gun_create, name='gun_create'),
    path('categories/', category_list, name='category_list'),
    path('<slug:slug>/edit/', gun_update, name='gun_update'),
    path('<slug:slug>/delete/', gun_delete, name='gun_delete'),
    path('category/create/', category_create, name='category_create'),
    path('category/<slug:slug>/edit/', category_update, name='category_update'),
    path('category/<slug:slug>/delete/', category_delete, name='category_delete'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('<slug:slug>/', gun_detail, name='gun_detail'),
]

