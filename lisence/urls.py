from django.urls import URLPattern, path
from .views import  obtain, ADobtain, TokenRequest, Deactveate
urlpatterns = [
    path('obtain/', obtain, name='obtain'),
    path('TokenRequest/', TokenRequest, name='TokenRequest'),
    path('Deactivate/', Deactveate, name='Deactivate'),
]