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


