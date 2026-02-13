from django.urls import path
from . import views

urlpatterns = [
    path('add/<slug:gun_slug>/', views.review_create, name='review_create'),
    path('<int:pk>/edit/', views.review_update, name='review_update'),
    path('<int:pk>/delete/', views.review_delete, name='review_delete'),
]
