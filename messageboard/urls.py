from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='board-home')
#    path('post/', views.createpost, name='post')

]