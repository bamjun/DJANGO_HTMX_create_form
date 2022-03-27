from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_views),
    path('<pk>/', views.index, name='index'),
]
