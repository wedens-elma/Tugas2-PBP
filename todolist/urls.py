from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', create_task, name='create-task'),
    path('status/', edit_status, name='edit_status'),
    path('hapus/', edit_status, name='edit_status'),
    
    # alternatif implementasi dari ka athal, lewat id passing
    path('status/<int:id>', ubah_status, name='ubah_status'),
    path('hapus/<int:id>', hapus_task, name='hapus_task'),

    # tugas 6
    path('change/<int:id>/', change_status, name='change_status'),
    path('delete-task-ajax/<int:id>/', delete_task_ajax, name='delete_task_ajax'),
    path('json/', show_json, name='show_json'),
    path('add/', create_task_ajax, name='create-task-ajax'),
]
