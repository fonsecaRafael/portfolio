from django.urls import path

from portfolio.knowledge.views import home

app_name = 'knowledge'
urlpatterns = [
    path('', home, name='home'),
]
