from django import forms

class NameForm(forms.Form):
    Name = forms.CharField(max_length=255)
    Email = forms.EmailField()
    Subject = forms.CharField()
    Message = forms.CharField(widget=forms.Textarea)