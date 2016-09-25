from django.conf.urls import url

from . import views

app_name = 'logbook'
urlpatterns = [
    # ex: /form/
    url(r'^$', views.index, name='index'),
    # ex: /form/login
    url(r'^login/$', views.login, name='login'),
]