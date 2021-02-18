from django import forms
from .models import PostQ


from django.conf import settings



       
class QuoteForm(forms.ModelForm):
    class Meta:
        model=PostQ
        fields=('author','body')

        widgets={
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control','rows':2}),
            
        }

        