from django.urls import path
from . import views

urlpatterns = [
    path('all', views.Get_all_entry),
    # path('add', views.Get_all_entry),
]