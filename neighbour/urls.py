
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^neighbourhood/(\d+)',views.neighbourhood,name ='neighbourhood'),
    url(r'^new/neighbourhood$', views.new_neighbourhood, name='new-neighbourhood')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)