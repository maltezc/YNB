from django.contrib.auth import  get_user_model
from rest_framework import generics, permissions, pagination
from accounts.api.permissions import AnonPermissionOnly
from rest_framework.response import Response

from books.api.serializers import BooksInLineUserSerializer
# from books.api.views import BookAPIView
from books.models import Books

from accounts.api.user.serializers import UserDetailSerializer

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    # permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset            = User.objects.filter(is_active=True)
    serializer_class    = UserDetailSerializer
    lookup_field        = 'username'

    def get_serializer_context(self):
        return {'request': self.request}


# class UserBookAPIView(BookAPIView):
#     serializer_class    = BooksInLineUserSerializer
    

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Books.objects.none()
        return Books.objects.filter(user__username=username)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here'"}, status=400)
