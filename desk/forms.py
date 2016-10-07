from django import forms
from desk.models import Task
 
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text']
 
