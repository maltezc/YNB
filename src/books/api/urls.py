from django.conf.urls import url, include
from .views import (
                BookAPIView,
                BookAPIDetailView,
                )


urlpatterns = [
    url(r'^$', BookAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', BookAPIDetailView.as_view(), name='detail'), #shift to id because of lookup field # <pk> is built in method for giving view id. api/status/12
]