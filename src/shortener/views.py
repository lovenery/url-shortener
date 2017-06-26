from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL

def kirr_redirect_view(request, shortcode=None, *args, **kwargs): # function based view FBV
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    # return HttpResponse("HI {sc}".format(sc=obj.url))
    return HttpResponseRedirect(obj.url)

class KirrRedirectView(View): # class based view CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponse("HI again {sc}".format(sc=obj.url))

    def post(self, request, *args, **kwargs):
        return HttpResponse()