from django.urls import path

from portfolio.projects.views import home

app_name = 'projects'
urlpatterns = [
    path('', home, name='home'),
]
