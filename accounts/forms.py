from event.models import *
from django import forms
from .models import *

class eventcreateForm(forms.ModelForm):


    def __init__(self, *args, **kargs):
        super(eventcreateForm, self).__init__(*args, **kargs)

    class Meta:
        model = general
        fields='__all__'


