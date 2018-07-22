from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^newprofile/',views.addprofile,name = 'addprofile'),
    url(r'^showprofile/(\d+)',views.showprofile,name = 'profile'),
    url(r'^imagepost/',views.addimages,name = 'imagepost'),

]
