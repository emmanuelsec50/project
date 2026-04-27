from django import forms
from .models import Members
class UpdateMemberForm(forms.ModelForm):
    class Meta:
        model=Members
        fields=['image', 'first_name', 'last_name', 'email']