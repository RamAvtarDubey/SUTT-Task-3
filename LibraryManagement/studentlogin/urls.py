from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),
    # path('', views.home, name='student-home'),
    path('about/', views.about, name='student-about'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
]