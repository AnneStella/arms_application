from django import forms
from my_app.models import Application


class ApplicantInfoForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'university', 'course', 'essay', 'resume',
                  'cover_letter',)
