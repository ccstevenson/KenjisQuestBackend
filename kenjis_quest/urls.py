from django.conf.urls import patterns, url, include
from apps.public.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('apps.public.views',

    url(r'^users$', UserList.as_view(), name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^create-user$', CreateUser.as_view(), name='create-user'),

    url(r'^characters$', CharacterList.as_view(), name='character-list'),
    url(r'^character/(?P<pk>[0-9]+)$', CharacterDetail.as_view(), name='character-detail'),
    url(r'^create-character$', CreateCharacter.as_view(), name='create-character'),

    url(r'^games$', GameList.as_view(), name='game-list'),
    url(r'^game/(?P<pk>[0-9]+)$', GameDetail.as_view(), name='game-detail'),
    url(r'^create-game$', CreateGame.as_view(), name='create-game'),

    url(r'^scenarios$', ScenarioList.as_view(), name='scenario-list'),
    url(r'^scenario/(?P<pk>[0-9]+)$', ScenarioDetail.as_view(), name='scenario-detail'),
    url(r'^create-scenario$', CreateScenario.as_view(), name='create-scenario'),

    url(r'^weapons$', WeaponList.as_view(), name='weapon-list'),
    url(r'^weapon/(?P<pk>[0-9]+)$', WeaponDetail.as_view(), name='weapon-detail'),
    url(r'^create-weapon$', CreateWeapon.as_view(), name='create-weapon'),

    url(r'^items$', ItemList.as_view(), name='item-list'),
    url(r'^item/(?P<pk>[0-9]+)$', ItemDetail.as_view(), name='item-detail'),
    url(r'^create-item$', CreateItem.as_view(), name='create-item'),

    url(r'^skills$', SkillList.as_view(), name='skill-list'),
    url(r'^skill/(?P<pk>[0-9]+)$', SkillDetail.as_view(), name='skill-detail'),
    url(r'^create-skill$', CreateSkill.as_view(), name='create-skill'),

    url(r'^races$', RaceList.as_view(), name='race-list'),
    url(r'^race/(?P<pk>[0-9]+)$', RaceDetail.as_view(), name='race-detail'),
    url(r'^create-race$', CreateRace.as_view(), name='create-race'),

    url(r'^nationalities$', NationalityList.as_view(), name='nationality-list'),
    url(r'^nationality/(?P<pk>[0-9]+)$', NationalityDetail.as_view(), name='nationality-detail'),
    url(r'^create-nationality$', CreateNationality.as_view(), name='create-nationality'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)