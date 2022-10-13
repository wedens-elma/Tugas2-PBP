from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse

from todolist.forms import Form

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    user = request.user
    context = {
        'list_task': data_todolist,
        'user': user,
    }
    return render(request, "todolist_ajax.html", context)

def show_xml(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = Form(request.POST)
    if request.method == 'POST':
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        return redirect('todolist:show_todolist')
    context = {'form': form}
    return render(request, "create-task.html", context)

# metode post pk dari task
def edit_status(request):
    if request.method == "POST":
        pk = request.POST.get("task_pk")
        task = Task.objects.get(pk = pk)
        action = request.POST.get("action")

        if request.user == task.user:
            if action == "finish":
                task.is_finished = True
                task.save()
            elif action == "unfinish":
                task.is_finished = False
                task.save()
            elif action == "delete":
                task.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

# alternatif implementasi dari ka Athal (thanks kak)
def ubah_status(request, id):
    status = Task.objects.get(pk=id)
    if status.is_finished:
        status.is_finished = False
    else:
        status.is_finished = True
    status.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def hapus_task(request, id):
    hapus = Task.objects.get(pk=id)
    hapus.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

# tugas 6
@login_required(login_url='/todolist/login/')
def create_task_ajax(request):
    if request.method == "POST":
        new_task = Task(
            date = datetime.datetime.now(),
            title = request.POST.get("title"),
            description = request.POST.get("description"),
            user = request.user
        )
        new_task.save()
        return HttpResponse(status=200)
    return redirect("todolist:show_todolist")

@login_required(login_url='/todolist/login/')
def delete_task_ajax(request: HttpRequest, id):
    if request.method == "DELETE":
        task = Task.objects.get(pk = id)

        if task.user == request.user:
            task.delete()
            response = HttpResponse(status=200)
        else:
            response = HttpResponse("Error: User not compatible", status=403)

        return response

    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def change_status(request, id):
    status = Task.objects.get(pk=id)
    if status.is_finished:
        status.is_finished = False
    else:
        status.is_finished = True
    status.save()
    return HttpResponse(serializers.serialize("json", [status]))
