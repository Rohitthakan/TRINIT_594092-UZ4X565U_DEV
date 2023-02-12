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
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('list', views.list, name='list'),
    path('dash', views.dash, name='dash'),
    path('feedback', views.feedback, name='feedback'),
    path('fundraising', views.fundraising, name='fundraising')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)