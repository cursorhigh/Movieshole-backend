from django.urls import path
from .views import google_auth, signnow , loginnow
urlpatterns = [
    path('google-auth/', google_auth, name='google_auth'),
    path('loginnow/', loginnow , name='loginnow'),
    path('signnow/',signnow,name='signnow'),
]
