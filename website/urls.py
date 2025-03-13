from django.urls import path
from django.contrib import admin
from . import views


urlpatterns=[
    path('',views.home_view,name='home'),
    path('admin/',admin.site.urls),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('record/<int:pk>',views.record_user,name='record'),
    path('delete/<int:pk>', views.delete_record, name='delete'),
    path('addRecord/', views.add_record, name='add_record'),
    path('update/<int:pk>',views.update_record,name='update')

]