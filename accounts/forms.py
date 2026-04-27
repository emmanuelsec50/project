from django import forms
from .models import Members, Messages
class UpdateMemberForm(forms.ModelForm):
    class Meta:
        model=Members
        fields=['image', 'first_name', 'last_name', 'email']
class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['content','image','audio']