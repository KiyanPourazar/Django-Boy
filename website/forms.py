from django import forms
from website.models import Contact, Newsletter

class NameForm(forms.Form):
    Name = forms.CharField(max_length=255)
    Email = forms.EmailField()
    Subject = forms.CharField()
    Message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    # last_name = forms.CharField(max_length=255)
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['Name', 'Email', 'Subject', 'Message']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'