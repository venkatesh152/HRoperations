from django import forms
from HRadmin.models import adminModel
import re

class adminForm(forms.ModelForm):
    passwod=forms.CharField(widget=forms.PasswordInput)

    dsg = [
        ('MANAGER', 'MANAGER'),
        ('HRhead', 'HRhead'),
        ('INTERVIWER', 'INTERVIWER'),
        ('EMPOYEE', 'EMPOYEE')
        ]
    desgination = forms.ChoiceField(choices=dsg)
    class Meta:
        model = adminModel
        fields = "__all__"

    def clean_passwod(self):
        pa=self.cleaned_data['passwod']
        re.findall(r'^[a-zA-Z0-9]+$',pa)

        if pa:
            return pa
        else:
            raise forms.ValidationError("Password contain in (a-z,A-z,0-9)")
