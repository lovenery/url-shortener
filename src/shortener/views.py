from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import KirrURL

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            "title": "Simplify your links",
            "form": form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Whoops!",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            # print("views.py, if form.is_valid(), form.cleaned_data: ", form.cleaned_data)
            new_url = form.cleaned_data.get("url")
            if not "http" in new_url:
                new_url = "http://" + new_url
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template, context)

class KirrRedirectView(View): # class based view CBV
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        ClickEvent.objects.create_event(obj)
        # return HttpResponse("URL: {sc}".format(sc=obj.url))
        return HttpResponseRedirect(obj.url)

    def post(self, request, *args, **kwargs):
        return HttpResponse()