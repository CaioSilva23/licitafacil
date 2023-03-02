from django.urls import path
from . import views


urlpatterns = [
    path('newslatter/', views.newslatter, name='newslatter'),
    path('email_contato/', views.email_contato, name='email_contato')
 
]
