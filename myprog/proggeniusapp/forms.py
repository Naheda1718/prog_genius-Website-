from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    phone = forms.CharField(max_length=20, label='Your Phone')
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=100, label='Subject', required=False)
    message = forms.CharField(widget=forms.Textarea, label='Your Message')