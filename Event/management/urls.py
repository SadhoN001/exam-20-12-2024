
from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from . import views 
from .views import EventDetailAPIView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    
    path('api/events/<int:pk>/', EventDetailAPIView.as_view(), name='event_detail_api'),
    
    path('event_list/', views.EventListView.as_view(), name='event_list'),
    path('create/', views.EventCreateView.as_view(), name='event_create'),
    path('update/<int:pk>/', views.EventUpdateView.as_view(), name='event_update'),
    path('delete/<int:pk>/', views.EventDeleteView.as_view(), name='event_delete'),
    path('register/<int:event_id>/', views.register_for_event, name='register_for_event'),
    
]