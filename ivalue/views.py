from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard'))

    return render(request, "landingpage.html", {})

def handler404(request):
    response = render_to_response('errors/404.html', {})
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('errors/500.html', {})
    response.status_code = 500
    return response
