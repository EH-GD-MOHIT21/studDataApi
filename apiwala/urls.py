from django.urls import path
from . import views
urlpatterns = [
    path('api/checkuser/<apikey>',views.APIWALA.as_view()),
    path('',views.home),
    path('signup',views.mainRegister),
    path('login',views.mainLogin),
    path('logmeout',views.mainLogout),
    path('resetpassword',views.resetpass),
    path('checkusernupdate',views.checknupdate),
    path('showmyapi',views.showapi),
]
