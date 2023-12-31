"""
URL configuration for Restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Food import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from Food import views as user_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('Menu', views.Menu,name='Menu'),
    path('Soups_Menu',views.Soups_Menu,name='Soups_Menu'),
    path('Starters_Menu',views.Starters_Menu,name='Starters_Menu'),
    path('Catering',views.Catering,name='Catering'),
    path('Feedback',views.Feedback,name='Feedback'),
    path('Booking',views.Booking,name='Booking'),
    path('feedbackdata',views.feedbackdata,name='feedbackdata'),
    path('bookingdata',views.bookingdata,name='bookingdata'),
    path('login',views.login,name='login'),
    path('Register',views.Register,name='Register'),
    path('useraccess',views.useraccess,name='useraccess'),
    path('adduser',views.adduser,name='adduser'),

]

urlpatterns+=staticfiles_urlpatterns()
