from django.urls import path
from django.contrib import admin
from . import views


urlpatterns=[
    path('',views.home_view,name='home'),
    path('admin/',admin.site.urls),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
]