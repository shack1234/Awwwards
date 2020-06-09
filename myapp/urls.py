from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^upload/$',views.upload_project,name='upload_project'),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'api/profiles/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    url(r'^post/(?P<project_id>[0-9]+)/review_design/$', views.rate_design, name='rate_design'),
    url(r'^post/(?P<project_id>[0-9]+)/review_usability/$', views.rate_usability, name='rate_usability'),
    url(r'^post/(?P<project_id>[0-9]+)/review_content/$', views.rate_content, name='rate_content'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'^profile/update/$', views.update_profile, name='update_profile'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'api/projects/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)