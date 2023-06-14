from django.contrib import admin
from django.urls import path
from book_api.views import book_list, book_create, book
from . import views



urlpatterns = [
    path('', views.book_create),
    path('list/', views.book_list),
    path('<int:pk>/', book),

]
