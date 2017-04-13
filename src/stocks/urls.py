from django.conf.urls import url, include

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from stocks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^tweet/', include('tweets.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
