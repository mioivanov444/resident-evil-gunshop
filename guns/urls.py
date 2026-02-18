from django.urls import path
from .views import gun_list, gun_detail, category_detail, gun_create, gun_update, gun_delete


urlpatterns = [
    path('', gun_list, name='gun_list'),
    path('add/', gun_create, name='gun_create'),
    path('<slug:slug>/edit/', gun_update, name='gun_update'),
    path('<slug:slug>/delete/', gun_delete, name='gun_delete'),
    path('<slug:slug>/', gun_detail, name='gun_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
]

