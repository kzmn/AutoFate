from django.conf.urls import patterns, include, url
from rest_framework import routers
from fate_game import views as game_views
from fate_skill import views as skill_views
from fate_character import views as character_views
from fate_aspect import views as aspect_views

router = routers.DefaultRouter()
router.register(r'games', game_views.GameViewSet)
router.register(r'skills', skill_views.SkillViewSet)
router.register(r'characters', character_views.CharacterViewSet)
router.register(r'player-characters', character_views.PlayerCharacterViewSet)
router.register(r'faces-and-places', character_views.FaceOrPlaceCharacterViewSet)
router.register(r'aspects', aspect_views.AspectViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^$', 'auto_fate.views.root_view'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
