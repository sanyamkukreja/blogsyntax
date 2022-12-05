from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.bloghome,name='bloghome'),
    path('<str:slug>',views.blogpost,name='post'),

    
]
