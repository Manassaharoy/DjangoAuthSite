from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'App_posts/home.html', context={'title':'Posts'})