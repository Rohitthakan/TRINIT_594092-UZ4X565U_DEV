from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from goodcauses import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('add', views.about, name='about'),
    path('resources', views.services, name='services'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('list', views.list, name='list'),
    path('dash', views.dash, name='dash'),
    path('feedback', views.feedback, name='feedback'),
    path('fundraising', views.fundraising, name='fundraising'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('http://127.0.0.1:8000/reset_password/<uidb64>/<token>', views.reset_password, name='reset_password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
