import json
from rest_framework import generics, mixins, permissions, viewsets
from rest_framework.authentication import SessionAuthentication # neccessary for user authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404,render


from accounts.api.permissions import IsOwnerOrReadOnly
from books.models import Books
from .serializers import BooksSerializer


# from __future__ import unicode_literals



def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class BookViewSet(viewsets.ViewSet):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    # authentication_classes  = []
    serializer_class        = BooksSerializer  # necessary
    queryset                = Books.objects.all()
    lookup_field            = 'id'
    search_fields           = ('user__username', 'content', 'user__email')
    ordering_fields         = ('user__username', 'timestamp')


# class BookAPIDetailView(
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.RetrieveAPIView):
#     permission_classes      = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    # authentication_classes  = []
#     serializer_class        = BooksSerializer  # necessary
#     queryset                = Books.objects.all()
#     lookup_field            = 'id'
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# # Login required mixin / decorator
# class BookAPIView(
#     mixins.CreateModelMixin,
#     generics.ListAPIView):
#     permission_classes          = [permissions.IsAuthenticatedOrReadOnly] # have to be logged in# if IsAuthenticatedOrReadOnly, non-logged in user cannot post, data is only read only # this demands that the person had to be authenticated inorder to do the things in this view. ie: create a post
#     serializer_class            = BooksSerializer #necessary
#     passed_id                   = None
#     search_fields               = ('user__username', 'content', 'user__email')
#     ordering_fields             = ('user__username', 'timestamp')
#     queryset                    = Books.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#         #comes from model mixin
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
