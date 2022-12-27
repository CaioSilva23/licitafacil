from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('email/', views.email, name='email'),
    path('contato/', views.contato, name='contato')
]
