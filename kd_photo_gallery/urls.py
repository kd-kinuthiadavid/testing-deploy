from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.all_images, name = 'welcome'),
    url(r'^$',views.painting_images, name = 'painting'),
    url(r'^image/(?P<image_id>\d+)', views.image, name="david"),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^$', views.all_images, name ='')
    # url(r'^$', views.projects_today, name='projectsToday'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_projects, name= 'past_days_projects'),
    # url(r'^search/', views.search_results, name='search_results'),
    # url(r'^project/(\d+)',views.project, name='project')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
