from django import forms
from myadmin import models

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = "__all__"
        exclude = ('user',)
        

class PackagesForm(forms.ModelForm):
    class Meta:
        model = models.Packages
        fields = "__all__"
        exclude = ('user',)