from django import forms
from .models import SignUp


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    #attach = forms.Field(widget=forms.FileInput)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['first_name', 'last_name', 'email', 'pan']

    def clean_email(self):
        email = (self.cleaned_data.get('email'))
        return email
        # email_base, provider = email.split("@")
        # domain, extension = provider.split('.')
        # if not extension == False:
        #     raise forms.ValidationError("Please use a valid email address.")
        # return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name

    def clean_pan(self):
        pan = self.cleaned_data.get('pan')
        return pan

        # def clean_date_of_birth(self):
        #      date_of_birth = self.cleaned_data.get('date_of_birth')
        #      return date_of_birth


