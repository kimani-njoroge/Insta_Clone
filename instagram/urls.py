from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^newprofile/',views.addprofile,name = 'addprofile'),
    url(r'^showprofile/(?P<user_id>\d+)',views.showprofile,name = 'profile'),
    url(r'^imagepost/',views.addimages,name = 'imagepost'),
    url(r'^search/',views.search_results, name = 'search_results'),
    url(r'follow/(?P<user_id>\d+)', views.follow, name='follow'),
    url(r'^comment/(?P<image_id>\d+)', views.addcomment, name='comment'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
