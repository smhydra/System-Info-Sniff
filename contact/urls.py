from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_text, name='upload'),
    path('success/', views.success, name='success'),
    path('submissions/', views.submissions, name='submissions'),
]
