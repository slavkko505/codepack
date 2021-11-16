from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'jewelry'
urlpatterns = [
    path('jewelry-list/', views.ShowAll, name='jewelry-list'),
    path('jewelry-detail/<int:pk>/', views.ViewProduct, name='jewelry-detail'),
    path('jewelry-create/', views.CreateProduct, name='jewelry-create'),
    path('jewelry-update/<int:pk>/', views.updateProduct, name='jewelry-update'),
    path('jewelry-delete/<int:pk>/', views.deleteProduct, name='jewelry-delete'),
]
