from django.conf.urls import url, include
from rest_framework import routers
from .views import (
                BookViewSet,
#                 BookAPIView,
#                 BookAPIDetailView,
                )


#todo: implement viewsets and routers for books


router = routers.SimpleRouter()
router.register(r'books', BookViewSet) # --> http://127.0.0.1:8000/api/books/api/books/

urlpatterns = [
    url(r'^api/', include(router.urls)),
    # url(r'^$', BookAPIView.as_view(), name='list'),
    # url(r'^(?P<id>\d+)/$', BookAPIDetailView.as_view(), name='detail'), #shift to id because of lookup field # <pk> is built in method for giving view id. api/status/12

]