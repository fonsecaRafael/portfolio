from django.urls import path, include

urlpatterns = [
    path('', include('portfolio.base.urls')),
    path('knowledge/', include('portfolio.knowledge.urls')),
]
