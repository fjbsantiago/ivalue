from django.conf.urls import url

from tweets import views

urlpatterns = [
    url(r'^$', views.TweetListView.as_view(), name='list'),
    url(r'^create', views.tweet_create_view, name='create'),
    url(r'^(?P<pk>\d+)', views.TweetDetailView.as_view(), name='detail'),
    #url(r'^update/1/$', views.TweetUpdateView.as_view(), name='update'),
    #url(r'^1/$', views.TweetDeleteView.as_view(), name='delete'),
]
