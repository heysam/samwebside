from django.conf.urls import url
#from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
#    url(r'^(\d+)/(\d+)/$',views.detail),

    # path(url, view, name=None)

]