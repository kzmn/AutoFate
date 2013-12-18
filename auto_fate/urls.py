from django.conf.urls import patterns, include, url
from rest_framework import routers
from fate_core import views

router = routers.DefaultRouter()
router.register(r'games', views.GameViewSet)
router.register(r'issues', views.IssueViewSet)
router.register(r'faces', views.FaceViewSet)
router.register(r'places', views.PlaceViewSet)
router.register(r'skills', views.SkillViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
