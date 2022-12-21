from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('current/', CurrentListView.as_view(), name='current'),
    path('create/', login_required(CreateTrackingView.as_view()), name='create'),
    path('complite/', CompliteListView.as_view(), name='complite'),
    path('personal/<int:pk>', PersonalAccountView.as_view(), name='personal'),
    path('update/<int:pk>', UpdateTrackingView.as_view(), name='update'),
    path('archive/<int:pk>', ArchiveTrackingView.as_view(), name='archive'),

]
