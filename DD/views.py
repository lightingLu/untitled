from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from DD.models import Event, Guest
from django.contrib import auth,sessions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect("/event_manage/")
            response.set_cookie('user', username, 3600)
            return response
            # if username == 'admin' and password == '123456':
            # response = HttpResponseRedirect("/event_manage/")
            # response.set_cookie('user', username, 3600)
            # request.session['user']=username
            # return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

def login_in_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect("/event_manage/")
            response.set_cookie('user', username, 3600)
            return response
            # if username == 'admin' and password == '123456':
            # response = HttpResponseRedirect("/event_manage/")
            # response.set_cookie('user', username, 3600)
            # request.session['user']=username
            # return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


def event_manage(request):
    event_list = Event.objects.all()
    username = request.COOKIES.get('user', '')
    return render(request, "event_manage.html", {"user": username, 'events': event_list})


def search_name(request):
    username = request.COOKIES.get('user', '')
    search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username, 'events': event_list})


def guest_manage(request):
    username = request.COOKIES.get("user", '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_mange.html", {"user": username, "guests": contacts})


def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)  # 默认调用Django的table.objects.get()方法，如果查询步存在则返回404错误
    return render(request, 'sign_index.html', {'event': event})


def sign_index_action(request, eid):
    event = get_object_or_404(Event, id=eid)  # 默认调用Django的table.objects.get()方法，如果查询步存在则返回404错误
    phone = request.POST.get('phone', '')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'Phone Error.'})
    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'Event ID or Phone Error.'})
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'User has sign in.'})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': 'Sign in Success.', 'guest': result})


def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response


def login_in(request):
    return render(request, "login_in.html")
