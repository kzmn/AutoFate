from django.conf.urls import patterns, include, url
from rest_framework import routers
from fate_core import views as core_views
from fate_character import views as character_views

router = routers.DefaultRouter()
router.register(r'games', core_views.GameViewSet)
router.register(r'issues', core_views.IssueViewSet)
router.register(r'faces', core_views.FaceViewSet)
router.register(r'places', core_views.PlaceViewSet)
router.register(r'skills', core_views.SkillViewSet)
router.register(r'characters', character_views.CharacterViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
