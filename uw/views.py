from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.utils import simplejson
from uw.forms import AddProgramForm, CreateActivityForm, UserProfileForm
from uw.models import Activity, Program
import random
import markdown


MEMCACHE_ACTIVITIES = 'activities'
items_per_page = 10

def list_activities(request):
    page_number = 1
    try:
        page_number = int(request.GET.get('p','1'))
    except ValueError:
        page_number = 1
    activities = cache.get(MEMCACHE_ACTIVITIES + str(page_number))
    if activities is None:
        activities = Activity.objects.all().order_by('-date')[(page_number-1)*items_per_page:page_number*items_per_page]
        cache.add(MEMCACHE_ACTIVITIES + str(page_number), activities)
    return direct_to_template(request, 'home.html',
                              {'activities': activities,
                               'form': CreateActivityForm()})

def create_activity(request):
    if request.method == 'POST' and request.user.is_authenticated():
        form = CreateActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            if request.user.is_authenticated():
                activity.author = request.user
            activity.save()
            for i in range(1, Activity.objects.all().count() / items_per_page + 2):
                cache.delete(MEMCACHE_ACTIVITIES + str(i))
    return HttpResponseRedirect('/home/')


@login_required
def home(request):
    user_profile = request.user.userprofile_set.all()
    return render_to_response('home.html', {'user': request.user,
                                            'userprofile': user_profile,
    }, context_instance=RequestContext(request))

def get(request, program_id):
    try:
        program = Program.objects.get(id=program_id)
        return render_to_response('program/get.html', {'user': request.user,
                                               'program': program},
        context_instance=RequestContext(request))
    except:
        return render_to_response('program/error.html', {'user':request.user},
                    context_instance=RequestContext(request))

@login_required
def add(request):
    if request.POST and request.POST.get('program_name'):
        new_program = Program.objects.get(name=request.POST.get('program_name'))
        request.user.userprofile_set.all().program.add(new_program)
        return HttpResponse('<li><a href="/program/'+str(new_program.id)+'">' + new_program.name + '</a></li>')
    return HttpResponse("")

@login_required
def lookup(request):
    # Default return list
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'query'):
            value = request.GET[u'query']
            # Ignore queries shorter than length 3
            if len(value) > 2:
                model_results = Program.objects.filter(name__startswith=value)
                results = [ x.name for x in model_results ]
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')


def login(request):
    redirect_to = settings.LOGIN_REDIRECT_URL
    return HttpResponseRedirect(redirect_to)
