from django.conf.urls import url, include
from django.contrib import admin

# from .views import UserDetailAPIView, UserBookAPIView

# if django 2.0, this looks different V
urlpatterns = [
#     url(r'^(?P<username>\w+)/$', UserDetailAPIView.as_view(), name='detail'),#user profile url
        #todo: User picture, about me, Books leased out, Books rented UserRating(pull from uber, airbnb?, lyft?)


    # url(r'^(?P<username>\w+)/status/$', UserBookAPIView.as_view(), name='book-list'), #user's book list
        #todo: show status of books with calendar for rental period

    #todo: Owner's Profile page(same page with viewing/editing priveleges)
    #todo: Owner's View Book list URL
        #todo: show how many times books have been rented, money made off of book, projected income?
]


