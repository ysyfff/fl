from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class UploadLFileForm(forms.Form):
    file = forms.FileField()