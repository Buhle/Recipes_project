from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details),
    url(r'^create$', views.create, name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

