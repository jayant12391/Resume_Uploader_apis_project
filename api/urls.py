from django.urls import path
from api import views

urlpatterns = [
    path('resume/', views.profileView.as_view(), name='resume'),
    path('list/', views.profileView.as_view(), name='list'),
]
