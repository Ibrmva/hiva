from django.urls import path, include
from . import views
urlpatterns = [
    #path('', views.login, name='home')
    path('signup', views.signup, name='home'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]