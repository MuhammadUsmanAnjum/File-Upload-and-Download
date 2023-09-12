from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.signup_view),
    path('login/', views.login_view),
]
