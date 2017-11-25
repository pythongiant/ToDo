from django import forms

class ToDo(forms.Form):
    ToDoInputBar = forms.CharField(label = "What Do You Want to do", max_length=10000)