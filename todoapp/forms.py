from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "myinput", "placeholder": "Enter Title"})) # type: ignore
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "paragraph", "placeholder": "Enter Description"})) # type: ignore
    class Meta:
        model = Task
        fields = ['title','description']