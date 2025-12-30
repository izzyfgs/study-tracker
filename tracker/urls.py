from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_score, name='add_score'),
    path('view/', views.view_scores, name='view_scores'),
]
