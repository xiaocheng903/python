from django import forms

class AppApplyForm(forms.Form):

    name = forms.CharField()

    name2 = forms.CharField()

    message = forms.CharField(widget=forms.Textarea)

