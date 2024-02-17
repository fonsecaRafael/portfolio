from django.urls import path, include

urlpatterns = [
    path('', include('portfolio.base.urls'))
]
