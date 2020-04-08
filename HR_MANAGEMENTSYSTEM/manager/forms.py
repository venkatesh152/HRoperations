from django import forms
from .models import recuirtmentModel,InterviewSeheduleModel

class recuirtmentform(forms.ModelForm):
    class Meta:
        model = recuirtmentModel
        fields = "__all__"

class InterviewSeheduleForm(forms.ModelForm):
    class Meta:
        model = InterviewSeheduleModel
        fields = "__all__"




