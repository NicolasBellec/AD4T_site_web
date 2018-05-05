from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nom", label_suffix="", max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="E-mail", label_suffix="", max_length=60, widget=forms.EmailInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label="Sujet", label_suffix="", max_length=60, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(label="Message", label_suffix="", max_length=2048, widget=forms.Textarea(attrs={'class':'form-control md-textarea', 'rows':'3'}))
