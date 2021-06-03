from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add/', views.add_picture, name='add_picture'),
    path('edit/<int:style_id>', views.edit_picture, name='edit_picture'),
    path('delete/<int:style_id>/', views.delete_picture, name='delete_picture'),
]
