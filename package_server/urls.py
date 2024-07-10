from django.shortcuts import render
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
  path('login/', views.login_view, name='login'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('', views.home_view, name='home'),
  path('add-package/', views.add_package_view, name='add_package'),
  path('add-library/', views.add_library_view, name='add_library'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('logout_page/', lambda request: render(request, 'logout.html'), name='logout_page'),
  path('api/package/<str:name>/', views.package_detail_view, name='package_detail_no_version'),
  path('api/package/<str:name>/<str:version>/', views.package_detail_view, name='package_detail_with_version'),
]