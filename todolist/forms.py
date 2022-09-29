from django.forms import ModelForm
from todolist.models import Task

class NewTask(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']