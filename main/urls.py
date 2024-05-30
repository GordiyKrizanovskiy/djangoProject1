from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('about/', views.about, name='about'),
]