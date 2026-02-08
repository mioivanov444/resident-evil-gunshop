from django.urls import path
from .views import gun_list, gun_detail

urlpatterns = [
    path('', gun_list, name='gun_list'),
    path('<slug:slug>/', gun_detail, name='gun_detail'),
]