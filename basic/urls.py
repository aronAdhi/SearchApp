from django.urls import path
from . import views

urlpatterns = [
    path('basic/', views.basic, name='basic'),
    path('ram/', views.ram, name='ram'),
    path('krishna/', views.krishna, name='krishna'),
    path('overall/', views.overall, name='overall'),
    path('hello/<str:name>/', views.say_hello, name='hello'),
    path('basic/details/<int:id>', views.details, name='details'),
]