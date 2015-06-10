from django.conf.urls import patterns, url, include

from .views import HouseholdList, DogOwnerList, HouseholdDetail, DogOwnerUpdate

urlpatterns = patterns('dogdate.views',
    url(r'^households$', HouseholdList.as_view(), name='households_list'),
    url(r'^households/(?P<household_pk>[0-9]+)/$', HouseholdDetail.as_view(),
            name="households_detail"),
    url(r'^dogowners$', DogOwnerList.as_view(), name='dogowners_list'),
    url(r'^dogowners/(?P<dogowner_pk>[0-9]+)$', DogOwnerUpdate.as_view(),
            name='dogowners_update'),
    url(r'^$', 'index', name='households_index'),
)
