from django import forms

from .models import Stock

class StockModelForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = [
            'content',
        ]

    """def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if content == "abc":
            raise forms.ValidationError("cannot be abc")

        return content"""
