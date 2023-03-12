from django import forms
from django.forms.renderers import TemplatesSetting

class CustomImageField(forms.ClearableFileInput):
    template_name = "views/"