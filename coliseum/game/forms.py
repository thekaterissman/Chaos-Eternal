from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    agree_to_terms = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(),
        label='I have read and agree to the User Agreement.'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)