from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return HttpResponseRedirect(reverse("test"))
    #     return super().get(request, *args, **kwargs)


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HowItWorksPage(TemplateView):
    template_name = 'HowItWorks.html'


from rest_framework import permissions, viewsets
from accounts.api.permissions import IsOwnerOrReadOnly
from books.models import Books
from .serializers import BooksSerializer
from rest_framework.response import Response



class BookViewSet(viewsets.ViewSet):
    # permission_classes      = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    # authentication_classes  = []
    # serializer_class        = BooksSerializer  # necessary
    # queryset                = Books.objects.all()
    # lookup_field            = 'id'
    # search_fields           = ('user__username', 'content', 'user__email')
    # ordering_fields         = ('user__username', 'timestamp')

    def list(self, request):
        return Response('Success')