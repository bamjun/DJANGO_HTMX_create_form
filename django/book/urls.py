from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_views),
    path('<pk>/', views.index, name='index'),
    path('htmx/create-form/', views.create_form, name='create-form'),
    path('htmx/<pk>/', views.detail_form, name='detail-form'),
    path('htmx/<pk>/delete_form', views.delete_form, name='delete-form'),
]
