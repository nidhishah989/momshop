from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store',views.store, name='store'),
    path('contact',views.contact, name='cont'),
    path('adminsm',views.artwork_list,name='artwork_list'),
    path(r'^artwork/(?P<id>[a-zA-Z0-9-]+)/$', views.artwork_detail, name='artwork_detail'),
    path('artwork/new/', views.artwork_new, name='artwork_new'),
    path(r'^artwork/edit/(?P<id>[a-zA-Z0-9-]+)/$', views.artwork_edit, name='artwork_edit'),
  
]