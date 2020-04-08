from django import forms
from .models import ApplicantModel,ApplicationformModel
gen=(
    ('male','MALE'),
    ('female','FEMALE')
)
posts=(

)
class ApplicantForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    class Meta:
        model = ApplicantModel
        fields ="__all__"

class Application_Form(forms.ModelForm):
    gender = forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    post=forms.ChoiceField(choices=posts)
    class Meta:
        model = ApplicationformModel
        fields ="__all__"
