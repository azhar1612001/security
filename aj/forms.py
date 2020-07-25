from django import forms
class CreateUserForm(forms.Form):
	enter_name=forms.CharField(required=False)