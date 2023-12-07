from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student', views.student , name='student'),
    path('student/add', views.student_add, name='student_add'),
    path('student/edit/<str:pk>', views.student_edit, name='student_edit'),
    path('student/delete/<str:pk>', views.student_delete, name='student_delete'),
    path('contact', views.contact , name='contact'),
]