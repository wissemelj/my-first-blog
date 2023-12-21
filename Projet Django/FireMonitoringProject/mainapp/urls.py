from django.urls import path
from .views import home, user_login
from .views import about_us_view 
urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
   path('about-us/', about_us_view, name='about_us'),
]
