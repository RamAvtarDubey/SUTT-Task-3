from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.home, name='choose_admin_or_student'),
    path('download_books/', views.download_books, name = 'download_books'),
    path('admin_login/', views.admin_login, name = 'admin_login'),
    path('upload_excel/', views.upload_excel, name = 'upload_excel'),
    path('student_login/', views.student_login, name = 'student_login'),
    path('done_uploading_excel/', views.done_uploading_excel, name = 'done_uploading_excel'),
    path('about/', views.about, name='student-about'),
    path('', views.home, name='student-home'),



]