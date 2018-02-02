from django.conf.urls import url

from heartbeat import views

urlpatterns = [
    url(r'^$', views.StatusView.as_view(), name='status'),
]
