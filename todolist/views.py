import datetime
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import NewTask
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    list_task = Task.objects.filter(user = request.user)
    context = {
        'username' : request.user.username,
        'task_list' : list_task,
    }
    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = NewTask()
    context = {'form': form}
    if request.method == 'POST':
        form = NewTask(request.POST)
        if form.is_valid():
            form_listener = form.save(commit=False)
            form_listener.user = request.user
            form_listener.save()
            return HttpResponseRedirect(reverse('todolist:show_todolist'))
        else:
            messages.info(request, 'Error when Entering Data!')

    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task = Task.objects.get(user=request.user, pk=id)
    task.delete()
    return redirect("todolist:show_todolist")

@login_required(login_url='/todolist/login/')
def update_task(request, id):
    task = Task.objects.get(user = request.user, pk = id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')