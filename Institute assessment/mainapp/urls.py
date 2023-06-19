"""
URL configuration for Institute_management project.

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
from django.urls import path,include
from mainapp import views

urlpatterns = [
   path('', views.home, name='home'),
   path('register/',views.register,name='register'),
   path('index/',views.index,name='index'),
   path('otp/',views.otp,name='otp'),
   path('login/',views.login,name='login'),
   path('logout/',views.logout,name='logout'),
   path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
   path('reset_password/',views.reset_password,name='reset_password'),
   path('forgot_otp/',views.forgot_otp,name='forgot_otp'),
   path('student/',views.student,name='student'),
   path('update_student\<int:pk>',views.update_student,name='update_student'),
   path('delete_student\<int:pk>',views.delete_student,name='delete_student'),
   path('teacher/',views.teacher,name='teacher'),
   path('update_teacher\<int:pk>',views.update_teacher,name='update_teacher'),
   path('delete_teacher\<int:pk>',views.delete_teacher,name='delete_teacher'),
   path('club/',views.club,name='club'),
   path('update_club\<int:pk>',views.update_club,name='update_club'),
   path('delete_club\<int:pk>',views.delete_club,name='delete_club'),
   path('book/',views.book,name='book'),
   path('update_book\<int:pk>',views.update_book,name='update_book'),
   path('delete_book\<int:pk>',views.delete_book,name='delete_book'),
   path('api/books/',views.booklist.as_view(),name='books'),
   path('api/books/<int:pk>',views.singlebooklist.as_view(),name='singlebooks'),

   
]
