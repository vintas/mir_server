from django.urls import path
from . import views

urlpatterns=[
  path('package',views.getPackageDetails),
  path('dependency',views.addDependency),
  path('',views.index)
]