from .models import *
from django import forms



class eventregform(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(eventregform, self).__init__(*args, **kargs)

    class Meta:
        model = eventregmodel
        fields='__all__'


class login_admin_form(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(login_admin_form, self).__init__(*args, **kargs)

    class Meta:
        model = login_admin
        fields='__all__'


class login_user_form(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(login_user_form, self).__init__(*args, **kargs)

    class Meta:
        model = login_user
        fields='__all__'

class UserRegForm(forms.ModelForm):


    def __init__(self, *args, **kargs):
        super(UserRegForm, self).__init__(*args, **kargs)

    class Meta:
        model = UserReg
        fields='__all__'



class AdminRegForm(forms.ModelForm):

    class Meta:
        model = AdminReg
        fields='__all__'












        



       
