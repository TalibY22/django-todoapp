from django import forms

class create_list(forms.Form):
    name = forms.CharField(label="task",max_length=200)
    check = forms.BooleanField(required=False)