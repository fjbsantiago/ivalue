from django.conf.urls import url
from stocks import views

urlpatterns = [
    url(r'^dashboard', views.dashboard, name='dashboard'),
]
