from django.conf.urls import url

from .views import ExpandAPIView, ParseAPIView


urlpatterns = [
    url(r'^expand/$',
        ExpandAPIView.as_view(),
        name='expand'),
    url(r'^parse/$',
        ParseAPIView.as_view(),
        name='parse'),
]
