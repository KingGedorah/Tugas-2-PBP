from django.urls import path
from todolist.views import update_task,delete_task, show_todolist, register, login_user, logout_user, create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist , name='show_todolist'),
    path('register/', register , name='register'),
    path('login/', login_user ,name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('create_task/', create_task, name='create_task'),
    path('delete/<int:id>/', delete_task , name='delete_task'),
    path('update/<int:id>/', update_task , name='update_task'),
]