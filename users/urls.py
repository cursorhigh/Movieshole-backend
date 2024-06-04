from django.urls import path
from .views import google_auth
from .views import loginnow
urlpatterns = [
    path('google-auth/', google_auth, name='google_auth'),
    path('loginnow/', loginnow , name='loginnow'),
]
