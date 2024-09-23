from django import forms
from myuser import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
        exclude = ('user','package','payment')


class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = "__all__"  
        exclude = ('user','package',)      