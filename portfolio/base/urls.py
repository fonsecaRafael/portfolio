from django.urls import path, include

from portfolio.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
]
