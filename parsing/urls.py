from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login, name='login'),
]
