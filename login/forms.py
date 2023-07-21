from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={'id':'login-username','placeholder':'Username'}),max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'login-password','placeholder':'Password'}))
    
