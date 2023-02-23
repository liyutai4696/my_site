from django.urls import path
from select_index import views

urlpatterns = [
    path('', views.select_index,name="select_index"),
]